const BASE_URL = 'http://0.0.0.0:8000/main'
let cityList = []


function clearFormInput (form) {
    $(':input', form)
        .not(':button, :submit, :reset, :hidden')
        .val('')
        .prop('checked', false)
        .prop('selected', false);
}

function loadCityList() {
    $.ajax({
        url: `${ BASE_URL }/city`,
        type: 'GET',
        dataType: 'json',
        success: function(res) {
            cityList = res
            res.forEach((i) => addCitiesTableRow(i))
        },
        error: function (err) {
            cityList = []
            clearCitiesTable()
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
    cols +=     `<button data-id="${ data.id }" type="button" class="btn btn-primary edit-item-button">Edit</button>`;
    cols +=     `<button data-id="${ data.id }" type="button" class="btn btn-danger ml-3 delete-item-button">Delete</button>`;
    cols += '</td>';

    newRow.append(cols);
    $(".table-cities").append(newRow);
    return false;
};

function clearCitiesTable() {
    $(".table-cities tr").remove();
}

$( document ).ready(function() {
    loadCityList()
    $('.save-create-changes-button').on('click', function (e) {
        let name = $('#create_name').val();
        let pollution_level_00 = $('#create_pollution_level_00').val();
        let pollution_level_01 = $('#create_pollution_level_01').val();
        let pollution_level_02 = $('#create_pollution_level_02').val();
        let industries = $('#create_industries').val();
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
                $('.modal').modal('hide');
                clearFormInput('#createForm')
                cityList.push(data)
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

    $(document).on('click', '.edit-item-button', function(event){
        let id = $(this).attr('data-id');
        let modal = $('#editModal');
        modal.attr('data-id', id)
        const city = cityList.find(i => String(i.id) === id)
        if(!city) return

        modal.find('#edit_name').val(city.name)
        modal.find('#edit_pollution_level_00').val(city.pollution_level_00)
        modal.find('#edit_pollution_level_01').val(city.pollution_level_01)
        modal.find('#edit_pollution_level_02').val(city.pollution_level_02)
        modal.find('#edit_industries').val(city.industries)
        modal.modal('show')
    });

    $(document).on('click', '.save-edit-changes-button', function(event){
        let modal = $('#editModal')
        let id = modal.attr('data-id')
        let name = $('#edit_name').val();
        let pollution_level_00 = $('#edit_pollution_level_00').val();
        let pollution_level_01 = $('#edit_pollution_level_01').val();
        let pollution_level_02 = $('#edit_pollution_level_02').val();
        let industries = $('#edit_industries').val();
        $.ajax({
            method: "PUT",
            url: `${ BASE_URL }/city/${ id }/`,
            data: {
                name,
                pollution_level_00,
                pollution_level_01,
                pollution_level_02,
                industries
            }})
            .done(function( data ) {
                modal.attr('data-id', '')
                clearCitiesTable()
                loadCityList()
                $('.modal').modal('hide');
                clearFormInput('#createForm')
            });
    });
});