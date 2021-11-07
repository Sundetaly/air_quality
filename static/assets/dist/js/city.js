const BASE_URL = 'http://0.0.0.0:8000/main'

function loadCityList() {
    $.ajax({
        url: `${ BASE_URL }/city`,
        type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {
            console.log(res);
            alert(res);
        }
    });
}

$( document ).ready(function() {
    loadCityList()
});