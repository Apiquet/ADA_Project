def updating_js_script(df, SCRIPT_PATH, markers_number=4, markers_speed=0.01, LatLong="[35.435804, 6.634183]", zoom="2"):
    
    simulation_duration = len(df.index)/markers_number/markers_speed
    protests_coordinates="" 
    protests_counts=""
    protests_types=""
    protests_dates=""
    marker_declaration=""
    string_addstation=""

    for marker_idx in range(1,markers_number+1):
        protests_coordinates = protests_coordinates + "\n var protests_coordinates" + str(marker_idx) + " = ["
        protests_dates = protests_dates + "\n var protests_dates" + str(marker_idx) + " = ["
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
        if 'count' in df:
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
    if 'count' in df:
        lines.append(protests_counts+'\n')
    lines.append(protests_dates+'\n')
    lines.append(protests_types+'\n')
    lines.append(marker_declaration+'\n')
    lines.append(string_addstation+'\n')
    w = open(SCRIPT_PATH + "script.js",'w')

    w.writelines([item for item in lines])

    w.close()