from jar import Jar
from pytest import raises


def test_init():
    jar = Jar(15)

    assert jar.capacity == 15


def test_str():
    jar = Jar(15)

    jar.deposit(3)

    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(15)

    jar.deposit(5)

    assert jar.size == 5

    with raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar(15)

    jar.deposit(5)
    jar.withdraw(3)

    assert jar.size == 2

    with raises(ValueError):
        jar.withdraw(10)
