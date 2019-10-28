

// Creating our initial map object
// We set the longitude, latitude, and the starting zoom level
// This gets inserted into the div with an id of 'map'
var myMap = L.map("map", {
    center: [38.58, -121.49],
    zoom: 13
  });
  
console.log("my map logic")

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);


var link = "static/data/stuff.geojson";

// Grab the data with d3
d3.json(link, function(response) {
  geodata = response.features
 // var features = [];
  console.log(geodata)
 // features = geoObject.features;
  
  console.log(geodata[0].geometry)
  // Create a new marker cluster group
 // console.log(  features)

  // Loop through the geodata array and create one marker for each item, 
  // bind a popup containing its title and age add it to the map
  
  for (var i = 0; i < geodata.length; i++) {
    var thing = geodata[i];
    L.marker(thing.geometry.coordinates)
      .bindPopup("<h1>" + thing.title + "</h1> <hr> <h3>Population " + thing.age + "</h3>")
      .addTo(myMap);
  }
  
});



