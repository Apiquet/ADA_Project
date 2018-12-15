import pandas as pd
import numpy as np
from math import pi
import matplotlib.pyplot as plt

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

def make_spider(chart_data, row, title, color):
    
    # number of variable
    categories=list(chart_data)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(3,4,row+1, polar=True, )

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    #ax.legend().set_visible(False)
    # Turn off tick labels
    ax.set_yticklabels([])
    #ax.set_xticklabels([])
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=40)

    # Draw ylabels
    #ax.set_rlabel_position(0)
    #plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
    plt.ylim(0,100)
    #filename='stats_per_region'+str(chart_data.loc[row]['Region'])+'.png'

    # Ind1
    values=chart_data.loc[row].drop('Region').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)
    plt.rcParams.update({'font.size': 500})

    # Add a title
    plt.title(title, size=60, color=color, y=1.1)
    #plt.savefig('maps/stats_regions/' + filename, dpi=96)
 
def get_df_for_countries_stats_visu(countries_all_stats, keep_US = True):
    chart_data = countries_all_stats[['Region',
     'Net migration',
     'Literacy (%)',
     'Agriculture',
     'Industry',
     'Service',
     'Birthrate',
     'Phones (per 1000)',
     'Infant mortality (per 1000 births)',
     'Pop. Density (per sq. mi.)',
     'Deathrate',
     'Arable (%)',
     'Crops (%)',
     'Income Group',
     'protests count']]
    #chart_data = chart_data.drop_duplicates(subset=['Region'], keep="first")
    chart_data = chart_data.groupby(['Region']).mean()
    chart_data = chart_data.reset_index()
    #chart_data = chart_data.drop('index',1)
    chart_data = chart_data.dropna()
    chart_data['Net migration'] = chart_data['Net migration'] + abs(min(chart_data['Net migration']))
    target_row = chart_data.ix[[7],:]
    chart_data=chart_data.drop([7])
    chart_data=chart_data.append(target_row)
    if keep_US == False:
        chart_data = chart_data[~chart_data['Region'].str.contains("NORTHERN AMERICA")]
    chart_data = chart_data.reset_index()
    chart_data = chart_data.drop('index',1)
    idx = 0
    for col in chart_data:
        if col == 'Region':
            continue
        chart_data[col] = chart_data[col].astype(float)
        chart_data[col] = chart_data[col] / max(chart_data[col]) * 100
    chart_data=chart_data.rename(columns={"Infant mortality (per 1000 births)": "Infant mortality","Income Group": "Income","Net migration": "Migration","Pop. Density (per sq. mi.)" :"Pop. Density", "Literacy (%)" : 'Literacy'})
    return chart_data

def convert_year_columns_to_one(data):
    data['GDP growth'] = 0
    data['year'] = 0
    data = data.loc[data.index.repeat(3)]
    move = 0
    col_p = 2
    for j in range(0,128):
        for i in range(0,3):
            data.iloc[i+move, data.columns.get_loc('GDP growth')] = data.iloc[i+move, col_p+i]
            data.iloc[i+move, data.columns.get_loc('year')] = list(data)[col_p+i]
        move = move + 3
    data = data.reset_index()
    data = data.drop(['index','2016','2017','2018','Country Code'], 1)
    data['year'] = data['year'].astype(str)
    data = data.loc[data.index.repeat(12)]
    move = 0
    for j in range(0,386):
        for i in range(0,12):
            if i < 9:
                data.iloc[i+move, data.columns.get_loc('year')] = data.iloc[i+move, data.columns.get_loc('year')] + '0' + str(i+1)
            else:
                data.iloc[i+move, data.columns.get_loc('year')] = data.iloc[i+move, data.columns.get_loc('year')] + str(i+1)       
        move = move + 12
    return data

def displaying_visu_countries_stat(new_data, DATA_PATH):
    my_dpi=96

    # For each year:
    for i in new_data.year.dropna().unique():

        # initialize a figure
        fig = plt.figure(figsize=(4050/my_dpi, 3000/my_dpi), dpi=my_dpi)

        plt.rcParams.update({'font.size': 50})
        plt.xlabel("Protests Count", fontsize=70)
        plt.ylabel("GDP growth", fontsize=70)
        plt.title("Month: "+str(i), fontsize=70 )

        # Change color with c and alpha. I map the color to the X axis value.
        tmp=new_data[ new_data.year == i ]

        plt.scatter(tmp['count'], tmp['GDP growth'] , s=10*tmp['pop_density'], c = tmp['region'].cat.codes.values, cmap="Accent", alpha=0.6, edgecolors="white", linewidth=2)
        #plt.legend()


        plt.ylim(-5,10)
        plt.xlim(-100,1100)
        #plt.legend(fontsize=50) # using a size in points
        #plt.legend(fontsize="x-large") # using a named size
        # Save it
        filename='GDP_growth_protests_count_'+str(i)+'.png'
        plt.savefig(DATA_PATH + filename, dpi=96)
        #plt.gca()

