QUnit.test("errors should be hidden on keypress", function (assert) {
    window.SuperLists.initialize();
    $('input[name="text"]').trigger('keypress');
    assert.equal($('.text-danger').is(':visible'), false);
    assert.equal($('#id_text').hasClass('is-invalid'), false);
});

QUnit.test("errors aren't hidded if there is no keypress", function (assert) {
    window.SuperLists.initialize();
    assert.equal($('.text-danger').is(':visible'), true);
    assert.equal($('#id_text').hasClass('is-invalid'), true);
});
