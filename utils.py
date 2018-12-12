import pandas as pd
import numpy as np

def text_to_df(filepath,press_freedom_df):

	
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
	return press_freedom_df      