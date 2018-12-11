import folium
import pandas as pd

def folium_map(df, x, y, location, countries_topodata, colormap, zoom=1):
    results_map_income = folium.Map(location, tiles='OpenStreetMap', zoom_start=zoom) 
    #creating dictionary to easily find the UDC voting rate
    dictionary = df.set_index(x)[y]#clean_data.set_index('CantonID')['UDC']
    #Our own choropleth 
    folium.TopoJson(
        countries_topodata,
    #     open('data/contries.topojson.json'),
        'objects.countries1',
        style_function=lambda x: {
            'fillColor': '#black' if (x['id'] not in dictionary.index.values) or (pd.isnull(dictionary[x['id']])) else colormap(dictionary[x['id']]),
            'color': 'black',
            'weight': 0.5,
            'dashArray': '5, 5',
            'fillOpacity': 0.9,
        },
        tooltip=folium.GeoJsonTooltip(fields=['name'],
                                      aliases=[''], 
                                      sticky=True, 
                                      style="font-family: Arial; color: black;", 
                                      opacity=0.8, 
                                      direction='top')
    ).add_to(results_map_income)
    results_map_income.add_child(colormap) #adding legend to map
    return results_map_income