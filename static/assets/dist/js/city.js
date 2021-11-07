const BASE_URL = 'http://0.0.0.0:8000/main'


function clearFormInput (form) {
    $(':input', form)
        .not(':button, :submit, :reset, :hidden')
        .val('')
        .prop('checked', false)
        .prop('selected', false);
}

function loadCityList(success, error) {
    $.ajax({
        url: `${ BASE_URL }/city`,
        type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {
            res.forEach((i) => addCitiesTableRow(i))
        },
        error: function (err) {
            console.log(err)
        }
    });
}

function addCitiesTableRow(data) {
    var newRow = $("<tr>");
    var cols = "";

    cols += `<td>${ data.id }</td>`;
    cols += `<td>${ data.name }</td>`;
    cols += `<td>${ data.pollution_level_00 }</td>`;
    cols += `<td>${ data.pollution_level_01 }</td>`;
    cols += `<td>${ data.pollution_level_02 }</td>`;
    cols += `<td>${ data.industries }</td>`;
    cols += '<td>';
    cols +=     `<button data-id="${ data.id }" type="button" class="btn btn-primary">Edit</button>`;
    cols +=     `<button data-id="${ data.id }" type="button" class="btn btn-danger ml-3 delete-item-button">Delete</button>`;
    cols += '</td>';

    newRow.append(cols);
    $(".table-cities").append(newRow);
    return false;
};


$( document ).ready(function() {
    loadCityList()
    $('.save-changes-button').on('click', function (e) {
        let name = $('#name').val();
        let pollution_level_00 = $('#pollution_level_00').val();
        let pollution_level_01 = $('#pollution_level_01').val();
        let pollution_level_02 = $('#pollution_level_02').val();
        let industries = $('#industries').val();
        $.ajax({
            method: "POST",
            url: `${ BASE_URL }/city/`,
            data: {
                name,
                pollution_level_00,
                pollution_level_01,
                pollution_level_02,
                industries
            }})
            .done(function( data ) {
                clearFormInput('#createForm')
                $('.modal').modal('hide');
                addCitiesTableRow(data)
            });
    })

    $(document).on('click', '.delete-item-button', function(event){
        let button = $(this);
        let id = $(this).attr('data-id');
        $.ajax({
            method: "DELETE",
            url: `${ BASE_URL }/city/${id}/`
        })
        .done(function() {
            button.parent().parent().remove()
        });
    });
});