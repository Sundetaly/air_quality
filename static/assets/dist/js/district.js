const BASE_URL = 'http://0.0.0.0:8000/main'
let districtList = []

function clearFormInput (form) {
    $(':input', form)
        .not(':button, :submit, :reset, :hidden')
        .val('')
        .prop('checked', false)
        .prop('selected', false);
}

function loadDistrictList(data = {}) {
    $.ajax({
        url: `${ BASE_URL }/district`,
        type: 'GET',
        dataType: 'json',
        data,
        success: function(res) {
            districtList = res
            res.forEach((i) => addDistrictsTableRow(i))
        },
        error: function (err) {
            districtList = []
            clearDistrictsTable()
        }
    });
}

function addDistrictsTableRow(data) {
    var newRow = $(`<tr data-id="${ data.id }">`);
    var cols = "";

    cols += `<td class="row-id">${ data.id }</td>`;
    cols += `<td class="row-name">${ data.name }</td>`;
    cols += `<td class="row-count_pesticide">${ data.count_pesticide }</td>`;
    cols += `<td class="row-name_pesticide">${ data.name_pesticide }</td>`;
    cols += `<td class="row-name_banned_pesticide">${ data.name_banned_pesticide }</td>`;
    cols += '<td>';
    cols +=     `<button data-id="${ data.id }" type="button" class="btn btn-primary edit-item-button">Edit</button>`;
    cols +=     `<button data-id="${ data.id }" type="button" class="btn btn-danger ml-0 ml-lg-1 mt-1 mt-lg-0 delete-item-button">Delete</button>`;
    cols += '</td>';

    newRow.append(cols);
    $(".table-districts tbody").append(newRow);
    return true;
};

function updateTableRow(data) {
    const itemRow = $(".table-districts").find(`tr[data-id="${data.id}"]`)
    if(!itemRow) return
    itemRow.find('.row-name').html(data.name)
    itemRow.find('.row-count_pesticide').html(data.count_pesticide)
    itemRow.find('.row-name_pesticide').html(data.name_pesticide)
    itemRow.find('.row-name_banned_pesticide').html(data.name_banned_pesticide)
    return true
}

function clearDistrictsTable() {
    $(".table-districts tbody").empty();
}

function clearFilters() {
    $('#filter_name').val('');
    $('#filter_count_pesticide').val('');
    $('#filter_name_pesticide').val('');
    $('#filter_name_banned_pesticide').val('');
}

$( document ).ready(function() {
    loadDistrictList()

    $('.search-button').on('click', function (e) {
        let name = $('#filter_name').val();
        let count_pesticide = $('#filter_count_pesticide').val();
        let name_pesticide = $('#filter_name_pesticide').val();
        let name_banned_pesticide = $('#filter_name_banned_pesticide').val();
        clearDistrictsTable()
        loadDistrictList({
            ...(name && { name }),
            ...(count_pesticide && { count_pesticide }),
            ...(name_pesticide && { name_pesticide }),
            ...(name_banned_pesticide && { name_banned_pesticide })
        })
    })
    $('.import-button').on('click', function (e) {
        $('.toast').toast('show');
        if(!$( '#fileImportInput' )[0]?.files?.[0]) return

        const data = new FormData();
        data.append( 'file', $( '#fileImportInput' )[0].files[0] );

        $.ajax({
            url: `${ BASE_URL }/district-import/`,
            data,
            processData: false,
            contentType: false,
            type: 'POST',
            success: function ( data ) {
                $('#fileImportInput').val(undefined);
                $('.modalImport').modal('hide');
                clearFilters()
                clearDistrictsTable()
                loadDistrictList()
            }
        });

        e.preventDefault();
    })

    $('.save-create-changes-button').on('click', function (e) {
        let name = $('#create_name').val();
        let count_pesticide = $('#create_count_pesticide').val();
        let name_pesticide = $('#create_name_pesticide').val();
        let name_banned_pesticide = $('#create_name_banned_pesticide').val();
        $.ajax({
            method: "POST",
            url: `${ BASE_URL }/district/`,
            data: {
                name,
                count_pesticide,
                name_pesticide,
                name_banned_pesticide
            }})
            .done(function( data ) {
                $('.modal').modal('hide');
                clearFormInput('#createForm')
                districtList.push(data)
                addDistrictsTableRow(data)
        });
    })

    $(document).on('click', '.delete-item-button', function(event){
        let button = $(this);
        let id = $(this).attr('data-id');
        $.ajax({
            method: "DELETE",
            url: `${ BASE_URL }/district/${id}/`
        })
        .done(function() {
            button.parent().parent().remove()
        });
    });

    $(document).on('click', '.edit-item-button', function(event){
        let id = $(this).attr('data-id');
        let modal = $('#editModal');
        modal.attr('data-id', id)
        const district = districtList.find(i => String(i.id) === id)
        if(!district) return

        modal.find('#edit_name').val(district.name)
        modal.find('#edit_count_pesticide').val(district.count_pesticide)
        modal.find('#edit_name_pesticide').val(district.name_pesticide)
        modal.find('#edit_name_banned_pesticide').val(district.name_banned_pesticide)
        modal.modal('show')
    });

    $(document).on('click', '.save-edit-changes-button', function(event){
        let modal = $('#editModal')
        let id = modal.attr('data-id')
        let name = $('#edit_name').val();
        let count_pesticide = $('#edit_count_pesticide').val();
        let name_pesticide = $('#edit_name_pesticide').val();
        let name_banned_pesticide = $('#edit_name_banned_pesticide').val();
        $.ajax({
            method: "PUT",
            url: `${ BASE_URL }/district/${ id }/`,
            data: {
                name,
                count_pesticide,
                name_pesticide,
                name_banned_pesticide
            }})
            .done(function( data ) {
                modal.attr('data-id', '')
                updateTableRow(data)
                districtList = districtList.map(i => String(i.id) === id ? data : i)
                $('.modal').modal('hide');
                clearFormInput('#createForm')
            });
    });
});