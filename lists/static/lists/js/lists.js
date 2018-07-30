window.SuperLists = {};

window.SuperLists.initialize = function() {
    $('input[name="text"]').on('keypress', function () {
        $('.text-danger').hide();
        $('#id_text').removeClass('is-invalid');
    });
};
