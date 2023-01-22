let jinjatrees = trees;




function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: { lat: 53.8059209, lng: -1.6758146 },
    });
    const infoWindow = new google.maps.InfoWindow({
      content: "",
      disableAutoPan: true,
    });
    
    markers = [];
    for (let tree of jinjatrees) {
      // Convert latitude and longitude into coords object {lat:x, lng: y}
      var coords = {lat:tree.latitude, lng:tree.longitude};
    
      var mk = new google.maps.Marker({
        position: coords,
        //Sets pins to drop onto screen animation
        animation:google.maps.Animation.DROP,
        // Icon set to "'PATH/tree' + '(GRADE)' + '.png'".   Doesn't seem to be case-sensitive
        icon: "static/TreeIcons/tree".concat(tree.grade,".png"),
        map,
        // TODO information like grade and who 'planted' it
        title: "Hello World!"
      });
      markers.push(mk);
    }
    

    
  
    // Add a marker clusterer to manage the markers.
    new markerClusterer.MarkerClusterer({ markers, map });
  }
  

  
  window.initMap = initMap;