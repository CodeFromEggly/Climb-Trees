function ipLocate() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(displayLocation);
    } else {
      // Geolocation is not supported by the browser
      console.log("Geolocation is not supported by this browser.");
    }

    function displayLocation(position) {
      var latitude = position.coords.latitude;
      var longitude = position.coords.longitude;
      
      // You can use the latitude and longitude values to display the user's location on a map, or to lookup the location name using a geocoding service
      document.getElementById("location").innerHTML = "Latitude: " + latitude + ", Longitude: " + longitude;
    }

  }