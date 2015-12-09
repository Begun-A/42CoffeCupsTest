function initAjaxForm() {
    $('#ajaxform').ajaxForm({
        success: function () {
            delete_errorlist();
            $("#success").show();
            setTimeout(function () {
                $("#success").hide();
            }, 5000);
        },
        error: function (response) {
            delete_errorlist();
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
function delete_errorlist() {
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