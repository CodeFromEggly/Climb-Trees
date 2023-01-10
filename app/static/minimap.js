
// Tests functionality using <p id="test"> in lcoation.html
var x = document.getElementById("test");
x.innerHTML="Whatever text!";
x.innerHTML = `${trees[0]['latitude']} Lat and ${trees[0]['longitude']} Lng`;

// TODO Obtain list of markers for trees:
markers = []

for (let i = 0; i < 10; i++) {
  var newTree = {
    lat:trees[i].latitude,
    lng:trees[i].long,
    id:trees[i].id
  }
  markers.push(newTree)
}
// TODO fill out tree database for further developing
markers.forEach(function(marker) {
  x.innerHTML += marker.lat;
});





function initMap(){
  var options = {
    zoom:4,
    center:{lat:-25.363, lng:131.844}
  }

  var map = new
  google.maps.Map(document.getElementById('map'), options);
}


// create marker function where 'options' = {coords:{lat:-x, lng:+y} icons:''}
function newMarker(options){
  var marker = new google.maps.marker({
    position:options.coords,
    map:map,
    icon:options.grade
  });
}


newMarker({coords:{lat:42.4668, lng:-70.9495}, icon:'https://github.com/CodeFromEggly/TreeHub/blob/main/TreeIcons/Tree%20Light%20Blue%203.png?raw=true'})
