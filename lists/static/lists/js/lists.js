window.SuperLists = {};

window.SuperLists.initialize = function() {
    $('input[name="text"]').on('keypress', function () {
        $('.is-invalid').hide();
    });
};
