let initialize = function() {
    $('input[name="text"]').on('keypress', function () {
        $('.is-invalid').hide();
    });
};
