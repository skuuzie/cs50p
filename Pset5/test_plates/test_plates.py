from plates import is_valid

def test_valid_with_num():
    assert is_valid("CS50") == True

def test_valid_without_num():
    assert is_valid("HELLO") == True

def test_valid_minimum_len():
    assert is_valid("HI") == True

def test_invalid_below_len_req():
    assert is_valid("A") == False

def test_invalid_exceed_len_limit():
    assert is_valid("THISISCS50") == False

def test_invalid_with_num_first():
    assert is_valid("11") == False

def test_invalid_with_num_inbetween():
    assert is_valid("CS50CS") == False

def test_invalid_with_zero_atfirst():
    assert is_valid("CS05") == False

def test_invalid_with_punct_n_space():
    assert is_valid("CS50.!") == False
