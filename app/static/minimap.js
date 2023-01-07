
// Tests functionality using <p id="test"> in lcoation.html
var x = document.getElementById("test");
x.innerHTML="Whatever text!";
x.innerHTML = `${trees[0]['latitude']} Lat and ${trees[0]['longitude']} Lng`;

// TODO Obtain list of markers for trees:
markers = []

for (let i = 0; i < 10; i++) {
  var newTree = {
    lat:trees[i]['latitude'],
    lng:trees[i]['longitude'],
    id:trees[i]['id']
  }
  markers.push(newTree)
}
// TODO fill out tree database for further developing



function initMap(){
  var options = {
    zoom:4,
    center:{lat:-25.363, lng:131.844}
  }

  var map = new
  google.maps.Map(document.getElementById('map'), options);
}



