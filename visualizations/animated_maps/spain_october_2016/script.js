// initialize the map on the "map" div with a given center and zoom
// create a new tile layer
var tileUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
layer = new L.TileLayer(tileUrl,
{
    attribution: 'Maps © <a href=\"www.openstreetmap.org/copyright\">OpenStreetMap</a> contributors',
    maxZoom: 15
});



var map = new L.Map('map', {center:[40.0,-4.0],zoom:6});map.addLayer(layer);

 var protests_coordinates1 = [[37.2714,-6.94946],[43.3,-2.98333],[43.2575,-2.9072299999999998],[40.4,-3.68333],[40.0,-4.0],[37.6,-4.5],[39.5,-3.0],[40.4,-3.68333],[40.4,-3.68333],[43.2575,-2.9072299999999998]]
 var protests_coordinates2 = [[41.3833,2.1833299999999998],[42.4333,-8.63333],[40.4,-3.68333],[43.3127,-2.67696],[36.7726,-4.10045],[39.6693,2.81487],[41.8831,-8.147219999999999],[37.1784,-3.5992],[40.4,-3.68333],[40.4,-3.68333]]
 var protests_coordinates3 = [[38.4,-5.35],[40.4,-3.68333],[39.5,-3.0],[41.3833,2.1833299999999998],[40.4,-3.68333],[39.889,-0.084989],[40.4,-3.68333],[40.4,-3.68333],[40.4,-3.68333]]
 var protests_coordinates4 = [[41.3833,2.1833299999999998],[40.4,-3.68333],[40.4,-3.68333],[40.4,-3.68333],[37.2879,-1.74901],[41.3833,2.1833299999999998],[40.4,-3.68333],[39.5,-3.0],[40.4,-3.68333]]
 var protests_coordinates5 = [[40.4,-3.68333],[37.6,-4.5],[41.3833,2.1833299999999998],[40.4,-3.68333],[40.4,-3.68333],[40.4,-3.68333],[40.4,-3.68333],[40.4,-3.68333],[40.4,-3.68333]]
 var protests_coordinates6 = [[40.0,-4.0],[40.4,-3.68333],[38.8779,-6.970610000000001],[40.0,-4.0],[43.2575,-2.9072299999999998],[41.3833,2.1833299999999998],[39.6693,2.81487],[40.4,-3.68333],[40.4,-3.68333]]
 var protests_coordinates7 = [[40.4,-3.68333],[41.3833,2.1833299999999998],[38.8779,-6.970610000000001],[40.0,-4.0],[40.4,-3.68333],[39.4333,-1.73333],[41.3833,2.1833299999999998],[41.3833,2.1833299999999998],[41.3833,2.1833299999999998]]

 var protests_counts1 = [[1],[1],[1],[9],[4],[2],[2],[19],[23],[3]]
 var protests_counts2 = [[1],[1],[7],[1],[1],[1],[1],[1],[24],[29]]
 var protests_counts3 = [[1],[4],[1],[5],[12],[1],[16],[20],[25]]
 var protests_counts4 = [[2],[5],[8],[10],[1],[6],[17],[3],[26]]
 var protests_counts5 = [[2],[1],[4],[11],[13],[15],[18],[21],[27]]
 var protests_counts6 = [[1],[6],[1],[2],[2],[7],[2],[22],[28]]
 var protests_counts7 = [[3],[3],[2],[3],[14],[1],[8],[9],[10]]

 var protests_dates1 = [[20160929],[20160929],[20160930],[20160930],[20160930],[20161001],[20161001],[20161002],[20161002],[20161002]]
 var protests_dates2 = [[20160929],[20160929],[20160930],[20160930],[20161001],[20161001],[20161001],[20161002],[20161002],[20161002]]
 var protests_dates3 = [[20160929],[20160929],[20160930],[20160930],[20161001],[20161001],[20161001],[20161002],[20161002]]
 var protests_dates4 = [[20160929],[20160929],[20160930],[20160930],[20161001],[20161001],[20161001],[20161002],[20161002]]
 var protests_dates5 = [[20160929],[20160929],[20160930],[20160930],[20161001],[20161001],[20161002],[20161002],[20161002]]
 var protests_dates6 = [[20160929],[20160930],[20160930],[20160930],[20161001],[20161001],[20161002],[20161002],[20161002]]
 var protests_dates7 = [[20160929],[20160930],[20160930],[20160930],[20161001],[20161001],[20161002],[20161002],[20161002]]

 var protests_types1 = [[141],[141],[141],[141],[140],[141],[141],[141],[141],[141]]
 var protests_types2 = [[141],[141],[141],[141],[141],[141],[141],[141],[141],[140]]
 var protests_types3 = [[141],[141],[141],[141],[141],[141],[141],[141],[141]]
 var protests_types4 = [[140],[141],[141],[141],[141],[141],[141],[141],[141]]
 var protests_types5 = [[141],[141],[141],[141],[141],[141],[140],[141],[141]]
 var protests_types6 = [[140],[141],[141],[140],[141],[140],[141],[141],[141]]
 var protests_types7 = [[141],[141],[141],[140],[141],[141],[140],[141],[141]]

 var marker1 = L.Marker.movingMarker(protests_coordinates1,protests_dates1,protests_types1,protests_counts1,94.28571428571428, {autostart: true}).addTo(map);
 var marker2 = L.Marker.movingMarker(protests_coordinates2,protests_dates1,protests_types2,protests_counts2,94.28571428571428, {autostart: true}).addTo(map);
 var marker3 = L.Marker.movingMarker(protests_coordinates3,protests_dates1,protests_types3,protests_counts3,94.28571428571428, {autostart: true}).addTo(map);
 var marker4 = L.Marker.movingMarker(protests_coordinates4,protests_dates1,protests_types4,protests_counts4,94.28571428571428, {autostart: true}).addTo(map);
 var marker5 = L.Marker.movingMarker(protests_coordinates5,protests_dates1,protests_types5,protests_counts5,94.28571428571428, {autostart: true}).addTo(map);
 var marker6 = L.Marker.movingMarker(protests_coordinates6,protests_dates1,protests_types6,protests_counts6,94.28571428571428, {autostart: true}).addTo(map);
 var marker7 = L.Marker.movingMarker(protests_coordinates7,protests_dates1,protests_types7,protests_counts7,94.28571428571428, {autostart: true}).addTo(map);

marker1.addStation(1, 500);marker1.addStation(2, 500);marker1.addStation(3, 500);marker1.addStation(4, 500);marker1.addStation(5, 500);marker1.addStation(6, 500);marker1.addStation(7, 500);marker1.addStation(8, 500);marker1.addStation(9, 500);marker1.addStation(10, 500);
marker2.addStation(1, 500);marker2.addStation(2, 500);marker2.addStation(3, 500);marker2.addStation(4, 500);marker2.addStation(5, 500);marker2.addStation(6, 500);marker2.addStation(7, 500);marker2.addStation(8, 500);marker2.addStation(9, 500);marker2.addStation(10, 500);
marker3.addStation(1, 500);marker3.addStation(2, 500);marker3.addStation(3, 500);marker3.addStation(4, 500);marker3.addStation(5, 500);marker3.addStation(6, 500);marker3.addStation(7, 500);marker3.addStation(8, 500);marker3.addStation(9, 500);
marker4.addStation(1, 500);marker4.addStation(2, 500);marker4.addStation(3, 500);marker4.addStation(4, 500);marker4.addStation(5, 500);marker4.addStation(6, 500);marker4.addStation(7, 500);marker4.addStation(8, 500);marker4.addStation(9, 500);
marker5.addStation(1, 500);marker5.addStation(2, 500);marker5.addStation(3, 500);marker5.addStation(4, 500);marker5.addStation(5, 500);marker5.addStation(6, 500);marker5.addStation(7, 500);marker5.addStation(8, 500);marker5.addStation(9, 500);
marker6.addStation(1, 500);marker6.addStation(2, 500);marker6.addStation(3, 500);marker6.addStation(4, 500);marker6.addStation(5, 500);marker6.addStation(6, 500);marker6.addStation(7, 500);marker6.addStation(8, 500);marker6.addStation(9, 500);
marker7.addStation(1, 500);marker7.addStation(2, 500);marker7.addStation(3, 500);marker7.addStation(4, 500);marker7.addStation(5, 500);marker7.addStation(6, 500);marker7.addStation(7, 500);marker7.addStation(8, 500);marker7.addStation(9, 500);
