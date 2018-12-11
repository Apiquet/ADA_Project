import pandas as pd
import numpy as np
np.random.seed(10)

def magnify():
    return [dict(selector="th",
                 props=[("font-size", "8pt")]),
            dict(selector="td",
                 props=[('padding', "0em 0em")]),
            dict(selector="th:hover",
                 props=[("font-size", "12pt")]),
            dict(selector="tr:hover td:hover",
                 props=[('max-width', '200px'),
                        ('font-size', '12pt')])]
def highlight_text(data, color='red', text = ''):
    '''
    highlight the maximum in a Series or DataFrame
    '''
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data.str.contains(text)
        return [attr if v else '' for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data.str.contains(text)
        return pd.DataFrame(np.where(is_max, attr, ''),
                            index=data.index, columns=data.columns)

def remove_randomly(df,n):
    drop_indices = np.random.choice(df.index, n, replace=False)
    df_subset = df.drop(drop_indices)
    return df_subset

def adding_count_of_repeated_values(df):
    for col in df:
        df[col] = df[col].astype(str)
    df['LatLong'] = df['ActionGeo_Lat'] + ',' + df['ActionGeo_Long']
    df['count'] = 0
    List = []
    count = []
    index = 0
    for value in df['LatLong']:
        if value in List:
            idx = List.index(value)
            count[idx] = count[idx] + 1
            df.iloc[index, df.columns.get_loc('count')] = count[idx]
        else:        
            List.append(value)
            count.append(1)        
            df.iloc[index, df.columns.get_loc('count')] = 1
        index = index + 1
    return df

def filtering_df_date_country(df, date_start, date_end,country = ' '):
    new_df = df[df.SQLDATE.astype(int) > date_start]
    new_df = new_df[new_df.SQLDATE.astype(int) < date_end]
    if country != ' ':
        new_df = new_df[new_df.ActionGeo_FullName.str.contains(country)]
    return new_df

def removing_duplicated_locations(df):
    size = len(df)
    for j in range(0,10):
        for index in range(0,size):
            if index == 0 :
                continue
            if index >= size:
                break
            value = df.iloc[index, df.columns.get_loc('count')] 
            if value < df.iloc[index-1, df.columns.get_loc('count')]:
                latlong = df.iloc[index, df.columns.get_loc('LatLong')]
                if latlong in df.iloc[index-1, df.columns.get_loc('LatLong')]:
                    df = df.drop(df.index[index])
                    index = index - 1
                    size = size - 1
    return df