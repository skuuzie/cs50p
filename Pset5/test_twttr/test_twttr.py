from twttr import shorten

def test_vowel():
    assert shorten("Twitter") == "Twttr"

def test_more_vowel():
    assert shorten("Facebook") == "Fcbk"

def test_numeric_omitting():
    assert shorten("Black123") == "Blck123"

def test_punct():
    assert shorten("Yo.") == "Y."

def test_combination():
    assert shorten("TwittEr!123") == "Twttr!123"
