from numb3rs import validate


def test_proper_ip():
    assert validate("192.168.1.1") == True


def test_string():
    assert validate("wow.wow.wow.100") == False


def test_out_of_bound():
    assert validate("192.168.1.256") == False


def test_out_of_boundv2():
    assert validate("512.512.512.512") == False
