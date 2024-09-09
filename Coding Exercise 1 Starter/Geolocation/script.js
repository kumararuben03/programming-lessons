let message = document.getElementById('message');

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
    message.innerHTML = `Latitude: ${lat}, Longitude: ${lng}`;
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