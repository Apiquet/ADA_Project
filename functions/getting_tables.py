import pandas as pd
import numpy as np
from math import pi
import matplotlib.pyplot as plt

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
            
            
   