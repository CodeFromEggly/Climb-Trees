
// Tests functionality using <p id="test"> in location.html
var x = document.getElementById("test");
x.innerHTML="Testing: ";

// TODO Process trees into a list called treeList:
treeList = [];

// Add each tree as a new marker to treeList
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

  treeList.push(newMarker);
}



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

  var map = new google.maps.Map(document.getElementById('map'), options);


  // Loop through treeList adding each one
  for (let i = 0, len = treeList.length; i < len; i++) {
    new google.maps.Marker({
      position: treeList[i].position,
      //Sets pins to drop onto screen animation
      animation:google.maps.Animation.DROP,
      // Icon set to "'PATH/tree' + '(GRADE)' + '.png'".   Doesn't seem to be case-sensitive
      icon: "static/TreeIcons/tree".concat(treeList[i].grade,".png"),
      map,
      // TODO information like grade and who 'planted' it
      title: "Hello World!"
    });

  }

}

