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