from um import count

def test_one():
    assert count("Um...") == 1

def test_zero():
    assert count("Uhm, the bumper is in the dump") == 0

def test_two():
    assert count("Um, are you sure about the, um... job?") == 2
