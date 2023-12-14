from bank import value

def test_hello():
    assert value("Hello") == 0

def test_first_letter_h():
    assert value("Hi") == 20

def test_no_h():
    assert value("Sup") == 100
