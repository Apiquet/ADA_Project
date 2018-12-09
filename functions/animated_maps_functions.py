import pandas as pd
def updating_js_script(df, SCRIPT_PATH, markers_number=4, markers_speed=0.01, LatLong="[35.435804, 6.634183]", zoom="2"):
    simulation_duration = len(df.index)/markers_number/markers_speed
    protests_coordinates="" 
    protests_counts=""
    protests_colors=""
    protests_types=""
    protests_dates=""
    marker_declaration=""
    string_addstation=""

    for marker_idx in range(1,markers_number+1):
        protests_coordinates = protests_coordinates + "\n var protests_coordinates" + str(marker_idx) + " = ["
        protests_dates = protests_dates + "\n var protests_dates" + str(marker_idx) + " = ["
        protests_colors = protests_colors + "\n var protests_colors" + str(marker_idx) + " = ["
        protests_counts = protests_counts + "\n var protests_counts" + str(marker_idx) + " = ["
        protests_types = protests_types + "\n var protests_types" + str(marker_idx) + " = ["
        addstation_idx = 0
        i = 0
        for idx in range(marker_idx,len(df),markers_number):
            i=i+1
            protests_coordinates = protests_coordinates + df["coord_for_js"].iloc[idx]
            protests_dates = protests_dates + df["dates"].iloc[idx]
            protests_types = protests_types + df["event_code"].iloc[idx]  
            if 'count' in df:
                protests_counts = protests_counts + df["count"].iloc[idx]
            if 'colors' in df:
                protests_colors = protests_colors + df["colors"].iloc[idx]

            if addstation_idx == 0 :
                    addstation_idx = 1
                    string_addstation = string_addstation + "\n"
            string_addstation = string_addstation + "marker" + str(marker_idx) + ".addStation(" + str(i) + ", 500);"

        #protests_df_for_js=protests_df_for_js.iloc[number_of_protests_per_loop:]
        protests_coordinates = protests_coordinates[:-1]
        protests_coordinates = protests_coordinates + "]"
        protests_dates = protests_dates[:-1]
        protests_dates = protests_dates + "]"  
        protests_types = protests_types[:-1]
        protests_types = protests_types + "]"
        protests_counts = protests_counts[:-1]
        protests_counts = protests_counts + "]"  
        protests_colors = protests_colors[:-1]
        protests_colors = protests_colors + "]"         
        if 'colors' in df:
            marker_declaration = marker_declaration + "\n var marker" + str(marker_idx) + " = L.Marker.movingMarker(protests_coordinates" + str(marker_idx) + ",protests_dates1,protests_colors"+ str(marker_idx) +"," + str(simulation_duration) + ", {autostart: true}).addTo(map);"
        elif 'count' in df:
            marker_declaration = marker_declaration + "\n var marker" + str(marker_idx) + " = L.Marker.movingMarker(protests_coordinates" + str(marker_idx) + ",protests_dates1,protests_types" + str(marker_idx) +",protests_counts"+ str(marker_idx) +"," + str(simulation_duration) + ", {autostart: true}).addTo(map);"
        else:
            marker_declaration = marker_declaration + "\n var marker" + str(marker_idx) + " = L.Marker.movingMarker(protests_coordinates" + str(marker_idx) + ",protests_dates1,protests_types" + str(marker_idx) +"," + str(simulation_duration) + ", {autostart: true}).addTo(map);"

    mapfit = 'var map = new L.Map(\'map\', {center:'+LatLong+',zoom:'+zoom+'});map.addLayer(layer);'
    
    readFile = open(SCRIPT_PATH + "script_origin.js")

    lines = readFile.readlines()
    lines = lines[:-1]
    readFile.close()
    
    lines.append(mapfit+'\n')
    lines.append(protests_coordinates+'\n')
    if 'colors' in df:
        lines.append(protests_colors+'\n')
    if 'count' in df:
        lines.append(protests_counts+'\n')
    lines.append(protests_dates+'\n')
    lines.append(protests_types+'\n')
    lines.append(marker_declaration+'\n')
    lines.append(string_addstation+'\n')
    w = open(SCRIPT_PATH + "script.js",'w')

    w.writelines([item for item in lines])

    w.close()
    
def converting_count_to_color(minimum, maximum, value):
    minimum, maximum = float(minimum), float(maximum)
    ratio = (value-minimum) / (maximum - minimum)
    b = 0
    r = 0
    g = 255
    if ratio < 0.2:
        b = 255 * (-5*ratio+1)
        r = 255 * (-2*ratio+1)
    else:
        g = 255 * (-1.66*ratio + 0.86)
    hexa = '#%02x%02x%02x' % (int(r), int(g), int(b))
    return '"' + hexa + '"'

def adding_count_columns(df):
    df['count'] = 0
    List = []
    count = []
    index = 0
    for value in df['coord_for_js']:
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

def getting_appropriate_format_df_for_js(df):
    #converting all columns to string
    for col in df:
        df[col] = df[col].astype(str)
    #getting a dataframe with appropriate format
    df_converted = pd.DataFrame()
    df_converted["coord_for_js"] = '[' + df['ActionGeo_Lat'] + ',' + df['ActionGeo_Long'] + '],'
    df_converted["dates"] = df['SQLDATE']
    df_converted["dates"] = '[' + df_converted['dates'].str[0:4] + df_converted['dates'].str[4:6] + df_converted['dates'].str[6:8] + '],'
    df_converted["event_code"] = df['EventCode']
    df_converted["event_code"] = '[' + df_converted['event_code'] + '],'
    for col in df_converted:
        df_converted[col] = df_converted[col].astype(str)
    return df_converted