let trees = jinjatrees;




function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: { lat: 53.8059209, lng: -1.6758146 },
    // TODO centre on device location (google has an API for this)7
  
    // Sets map type to Hybrid by default
    mapTypeId: google.maps.MapTypeId.HYBRID
  });

  const infoWindow = new google.maps.InfoWindow({
    content: "",
    disableAutoPan: true,
  });

  // If device allows access to location, centre map on its position.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
        initialLocation = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
        map.setCenter(initialLocation);
        map.setZoom(4)
    });
  }
    
  markers = [];
  for (let tree of trees) {
    // Convert latitude and longitude into coords object {lat:x, lng: y}
    var coords = {lat:tree.latitude, lng:tree.longitude};
  
    var mk = new google.maps.Marker({
      position: coords,
      id: tree.id,
      grade: tree.grade,
      planter: tree.planter,
      icon: "static/TreeIcons/tree".concat(tree.grade,".png"),

      //Sets pins to drop onto screen animation
      animation:google.maps.Animation.DROP,
      
      map,
      title: `Tree  ${tree.id}!`
    });
    markers.push(mk);
  }
    

    
  
  // Add a marker clusterer to manage the markers.
  new markerClusterer.MarkerClusterer({ markers, map });

  
  }
  

  
  window.initMap = initMap;