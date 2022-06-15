from main import main_menu, entrypoint, order, view_cart, cancel_order, view_order

def test_main(capfd):
    main_menu()
    out, err = capfd.readouterr()
    assert type(out) == str

def test_entry(capfd):
    entrypoint() 
    out, err = capfd.readouterr()
    assert type(out) == str

def test_order(capfd):
    order() 
    out, err = capfd.readouterr()
    assert type(out) == str

def test_cart(capfd):
    view_cart()
    out, err = capfd.readouterr()
    assert type(out) == str

def test_cancel(capfd):
    cancel_order()
    out, err = capfd.readouterr()
    assert type(out) == str

def test_view_order(capfd):
    view_order()
    out, err = capfd.readouterr()
    assert type(out) == str
