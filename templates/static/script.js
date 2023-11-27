function sendUSB0() {
    var value = document.getElementById('usbstorage0').value; 
    $.ajax({ 
        url: '/process', 
        type: 'POST', 
        contentType: 'application/json', 
        data: JSON.stringify({ 'value': value }), 
        success: function(response) { 
            console.log(response.result);
        }, 
        error: function(error) { 
            console.log(error); 
        } 
    }); 
}