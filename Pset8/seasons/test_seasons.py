from seasons import convert_date_gap_to_minutes
from pytest import raises

def test_valid():
    assert convert_date_gap_to_minutes("2022-12-11") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_date_gap_to_minutes("2021-12-11") == "One million, fifty-one thousand, two hundred minutes"

def test_invalid_format():
    with raises(SystemExit):
        convert_date_gap_to_minutes("December 10th, 2000")

def test_invalid_month():
    with raises(SystemExit):
        convert_date_gap_to_minutes("2000-13-13")
