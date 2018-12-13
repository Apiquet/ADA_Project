import pandas as pd
import numpy as np
from math import pi
import matplotlib.pyplot as plt


def country_stat_creation(protests_df,country_by_income_2017,countries_stats,country_codes_to_name):
        #Getting number of protests per country without any threshold
    number_of_protests_per_country = protests_df.groupby(['Country Code']).size().reset_index(name='protests count')

    #Extracting the two column we are interesting in
    country_by_income_2017_filtered=country_by_income_2017[['Country Code','Income Group']]

    #joining tables to get the country, the income group and the protests count in the same table
    income_group_and_protests_count=pd.merge(country_by_income_2017_filtered, number_of_protests_per_country, how='right', on=['Country Code'])
    


    countries_stats_with_code=pd.merge(countries_stats, country_codes_to_name, how='left', on='Country Name')
    countries_stats_with_code=countries_stats_with_code.dropna()

    #Getting a dataframe with all the statistics by country!
    countries_all_stats=pd.merge(countries_stats_with_code, income_group_and_protests_count, how='left', left_on='Country Code', right_on='Country Code')
    countries_all_stats=countries_all_stats.dropna()
    #Using countries that have more than 1 protest for the linear regression
    countries_all_stats=countries_all_stats[countries_all_stats['protests count'] > 1]
    return countries_all_stats
    

def load_countrycode(DATA_PATH):
        #Getting conversion between fips104 and iso2 code for countries
    country_codes_fips104_to_iso = pd.read_csv(DATA_PATH + "fips104_to_iso.csv", encoding = "ISO-8859-1")

    #Getting conversion between iso2 and iso3 code for countries
    country_codes_iso2_to_iso3 = pd.read_csv(DATA_PATH + "country_codes_iso2_to_iso3.csv", encoding = "ISO-8859-1")

    #merging the two data to convert from Fips 104 to ISO3
    country_codes_fips104_to_iso3 = pd.merge(country_codes_fips104_to_iso, country_codes_iso2_to_iso3, how='inner',\
                                             left_on=['ISO 3166'], right_on=['ISO'])[['FIPS 10-4', 'ISO3']]

    # Getting conversion between country code and country name
    country_codes_to_name = pd.read_csv(DATA_PATH + "country_lat_long.csv", encoding = "ISO-8859-1")
    country_codes_to_name=country_codes_to_name.rename(index=str, columns={"ISO3": "Country Code"})
    country_codes_fips104_to_iso3=country_codes_fips104_to_iso3.rename(index=str, columns={"ISO3": "Country Code"})
    return country_codes_to_name, country_codes_fips104_to_iso3

def open_and_clean_data(DATA_PATH):
    hdi_df = pd.read_csv(DATA_PATH + "Human_Development_Index_(HDI).csv", encoding = "ISO-8859-1")
    hdi_df = hdi_df.drop(hdi_df.iloc[:,2:17], axis = 1)
    
    gini_df = pd.read_csv(DATA_PATH + "GINI_per_country_worldbank.csv", encoding = "ISO-8859-1")
    gini_df = gini_df.drop(gini_df.iloc[:,2:49], axis = 1)
    
    gdp_df = pd.read_csv(DATA_PATH + "GDP_growth_world_bank.csv", encoding = "ISO-8859-1")
    gdp_df = gdp_df.drop(gdp_df.iloc[:,2:49], axis = 1)
    
    corruption_df = pd.read_csv(DATA_PATH + "DataCorruptionPerceptionIndex2000_2017.csv", encoding = "ISO-8859-1")
    corruption_df = corruption_df.drop(corruption_df.iloc[:,1:6], axis = 1)

    
    #initilize empty dataframe with corresponding columns
    columns_data=['Country','2018', '2017', '2016', '2015', '2014','2013', '2012','2011', '2010', '2009','2008', '2007', '2006', '2005', '2004','2003', '2002']
    press_freedom_df =  pd.DataFrame(columns = columns_data, index = range(0,200))
    
    filepath = DATA_PATH+'parse.txt'   
    #press_freedom_df
    index = []
    values = []


    with open(filepath) as fp:  
        line = fp.readline()
        column = 0
        cnt = 0
        line = fp.readline()


        while cnt <= 179: #179 counrty in the file


            if(line[0] == ' '): #if we detect the space in front of country name
                cnt+=1 # row = row + 1
                column = 0
                values.append(line.split('\t')[0]) #Only keep the name of the counrty and not the shifted rank
                line = fp.readline()
            else:
                while(line[0] != ' '): #While these are the index correspnding to the country detected above

                    column += 1
                    values.append(line.split()[0]) #Only keeps the index and not the ranking

                    line = fp.readline()

                row = pd.Series( (v for v in values) )
                values = []

                n = 0
                for i in range(len(row)):
                    if(i == 0):
                        press_freedom_df['Country'].iloc[cnt] = row.iloc[0] #name in country column
                    else:
                        if(2019 - i == 2011):
                            n = 1
                        press_freedom_df[str(2019-i-n)].iloc[cnt] = row.iloc[i] # index corresponding to year


    fp.close()   
    
    
    press_freedom_df = press_freedom_df.drop(0)
    press_freedom_df = press_freedom_df.head(179)
    
    
    """For press freedom This looks really messy, but in fact, the values under each country name are the indices from 2018 t 2002 and the number in parenthsis is the rank for each year. We create a dataframe with press-freedom indices corresponding to each country and each year.

In the algorithm bellow we parse these data to generate the dataframe

According to wikipeddia, 2011 is missing because the report released in 2012 is titled '2011–2012' and cover both 2011 and 2012 in one column. We will later see what we can do to recover these missing data."""
    
    return press_freedom_df, hdi_df, gini_df, gdp_df,corruption_df        
            
            
   