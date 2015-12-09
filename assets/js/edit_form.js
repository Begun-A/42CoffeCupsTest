function initAjaxForm() {
    $('#ajaxform').ajaxForm({
        beforeSubmit: function(form, options) {
            block_form();
        },
        success: function () {
            unblock_form();
            $("#success").show();
            setTimeout(function () {
                $("#success").hide();
            }, 5000);
        },
        error: function (response) {
            unblock_form();
            $("#form_error").show();
            var errors = JSON.parse(response.responseText);
            for (error in errors) {
                var id = '#id_' + error;
                $(id).parent('p').append(errors[error]);
                console.log(id);
                console.log(errors[error]);
                console.log($(id).prepend(errors[error]))

            }
            setTimeout(function () {
                $("#form_error").hide();
            }, 5000);
        }
    });
}
function block_form() {
        $("#loading").show();
        $('textarea').attr('disabled', 'disabled');
        $('input').attr('disabled', 'disabled');
}

function unblock_form() {
    $('#loading').hide();
    $('textarea').removeAttr('disabled');
    $('input').removeAttr('disabled');
    $('.errorlist').remove();
}
function readURL() {
    var input = this;
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $(".image").attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);}}

$(function () {
    $("#id_photo").change(readURL)});

$(document).ready(function() {
    initAjaxForm();

});