function init(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    }
    else{
        message.innerHTML = 'Geolocation is not supported in this browser.';
    }
}

function showPosition(position){
    let lat = position.coords.latitude;
    let lng = position.coords.longitude;

    let map = L.map('map').setView([lat, lng], 14);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 20,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    let marker1 = L.marker([lat, lng]).addTo(map);

    marker1.bindPopup("<b>My Current Location</b>", {closeOnClick: false, autoClose:false}).openPopup();
    
}

function showError(err){
    switch(err.code){
        case err.PERMISSION_DENIED:
            message.innerHTML = 'User denied the request for Geolocation.';
            break;
        case err.POSITION_UNAVAILABLE:
            message.innerHTML = 'Location information is unavailable.';
            break;
        case err.TIMEOUT:
            message.innerHTML = 'The request to get user location timed out.';
            break;
        case err.UNKNOWN_ERROR:
            message.innerHTML = 'An unknown error occurred.';
            break;
    }
}

init();