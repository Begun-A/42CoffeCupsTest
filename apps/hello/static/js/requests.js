var lost_focus, count = 0, title = document.title;
function initUpdateRequests() {

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
            var n = new_table.find('#request-id').html() - table.find('#request-id').html();
            table.find('table').html(new_table.html());
            count = count + parseInt(n.toString());
            if (lost_focus) {
                if (count == 0) {
                    document.title = title
                }
                else {
                    document.title = count.toString() + ' New ' + title;
                }
            }
            else {
                count = 0;
                document.title = title;
            }
        },
        'error': function () {
            alert('Error on the server');
            return false;
        }
    });
    return false
}

$(document).ready(function () {
    setInterval('initUpdateRequests()', 50000);

    $(window).blur(function () {
        lost_focus = true;
    });
    $(window).focus(function () {
        lost_focus = false;
    });
});


