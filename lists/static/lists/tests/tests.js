QUnit.test("errors should be hidden on keypress", function (assert) {
    window.SuperLists.initialize();
    $('input[name="text"]').trigger('keypress');
    assert.equal($('.is-invalid').is(':visible'), false);
});

QUnit.test("errors aren't hidded if there is no keypress", function (assert) {
    window.SuperLists.initialize();
    assert.equal($('.is-invalid').is(':visible'), true);
});
