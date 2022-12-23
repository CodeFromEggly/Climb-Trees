navigator.geolocation.watchPosition(function(position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    var accuracy = position.coords.accuracy;
  
    // create a marker for the device's location
    var marker = L.marker([lat, lng]).addTo(map);
  
    // update the marker position as the device moves
    marker.setLatLng([lat, lng]);
  
    // update the map view to center on the marker
    map.panTo([lat, lng]);
  }, function(error) {
    console.error(error);
  });
  