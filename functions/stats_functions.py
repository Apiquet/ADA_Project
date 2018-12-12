import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

def regression(data, X_features, y_feature):
    X = data[X_features]
    X2 = sm.add_constant(X)
    y = data[y_feature]
    est = sm.OLS(y, X2)
    est2 = est.fit()
    print(est2.summary())

def show_nb_protest_per_month(data, CountryCode, year, y_label ='Nb protests'):
    months = np.array(['Jan', 'Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    temp = data[(data['Year']==year) & (data['Country Code']==CountryCode)]
    protests_month_per_country = temp.groupby(['Country Code', 'MonthYear']).agg({'ID': 'count'})
    protests_month_per_country.reset_index(inplace=True)
    protests_month_per_country.rename(columns={'ID': 'Nb protests'}, inplace=True)
    protests_month_per_country['Month'] = months[list(protests_month_per_country['MonthYear'].index)]
    protests_month_per_country.plot(x='Month', y='Nb protests', kind='bar', colormap='Paired', legend=None)
    plt.ylabel(y_label)
