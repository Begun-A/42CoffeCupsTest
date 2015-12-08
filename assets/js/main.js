function initUpdateRequests(){

    var link = $(this);
    $.ajax({
        'url': link.attr('href'),
        'type': 'GET',
        'dataType': "html",
        'success': function (data, status, xhr) {
            if (status != 'success') {
                alert('Error on the server');
                return false;
            }
            var table = $('#div_table1'), html = $(data), new_table = html.find('table');
            table.find('table').html(new_table.html());
        },
        'error': function () {
            alert('Error on the server');
            return false;
        }
    });
    return false
};

$(document).ready(function(){
    setInterval('initUpdateRequests()',5000);
});
