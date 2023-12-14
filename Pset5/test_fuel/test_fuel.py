from fuel import convert, gauge
from pytest import raises

def test_convert():
    assert convert("4/4") == 100
    assert convert("1/2") == 50

    with raises(ZeroDivisionError):
        convert("4/0")

    with raises(ValueError):
        convert("2/1")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"

