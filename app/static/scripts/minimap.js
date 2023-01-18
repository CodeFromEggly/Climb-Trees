
// Tests functionality using <p id="test"> in location.html
var x = document.getElementById("test");
x.innerHTML="Testing: ";

// TODO Process trees into a list called markers:
markers = []

// Add each tree as a new marker to markers
let jinjatrees = trees
for (let tree of jinjatrees) {
  // Convert latitude and longitude into coords object {lat:x, lng: y}
  var coords = {lat:tree.latitude, lng:tree.longitude};
  var newMarker = {
    position: coords,
    id: tree.id,
    grade: tree.grade,
    planter: tree.planter
  };
  markers.push(newMarker);
}

x.innerHTML += markers[0].position;


// Create the map
function initMap(){
  // Set options for the map
  var options = {
    center:{lat:53.6490, lng:-1.7842},
    zoom:4,
    // TODO centre on device location (google has an API for this)
    // Sets map type to Hybrid by default
    mapTypeId: google.maps.MapTypeId.HYBRID
  };

  var map = new
  google.maps.Map(document.getElementById('map'), options);
 
  // Loop through markers adding each one
  for (let i = 0, len = markers.length; i < len; i++) {
    new google.maps.Marker({
      position: markers[i].position,
      //Sets pins to drop onto screen animation
      animation:google.maps.Animation.DROP,
      //sets icon displayed maybe a check for diffrent grades
      icon: "https://raw.githubusercontent.com/CodeFromEggly/TreeHub/Flask-branch/app/static/TreeIcons/Tree%20Black%209%2060%2040.png",
      map,
      // TODO information like grade and who 'planted' it
      title: "Hello World!"
    });
  }
}

