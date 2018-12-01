// initialize the map on the "map" div with a given center and zoom
var map = new L.Map('map', {
  zoom: 3
});

// create a new tile layer
var tileUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
layer = new L.TileLayer(tileUrl,
{
    attribution: 'Maps © <a href=\"www.openstreetmap.org/copyright\">OpenStreetMap</a> contributors',
    maxZoom: 15
});

// add the layer to the map
map.addLayer(layer);

var mapfit = [[-50, 70], [-50, 80],[50, -90], [80, 80], [-50, 130]];
map.fitBounds(mapfit);

