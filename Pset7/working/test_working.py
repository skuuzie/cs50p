from working import convert
from pytest import raises

def test_valid():
    assert convert("7 PM to 7 AM") == "19:00 to 07:00"

def test_valid_with_minute():
    assert convert("7:25 PM to 1:22 AM") == "19:25 to 01:22"

def test_invalid_minute():
    with raises(ValueError):
        convert("7:60 PM to 7 AM")

def test_invalid_format():
    with raises(ValueError):
        convert("7:30 PM - 7 AM")

def test_twelve():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
