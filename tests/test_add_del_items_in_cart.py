def test_add_del_items_in_cart(app):
    for i in range(3):
        app.add_items_in_cart()
    app.del_items_from_cart()
