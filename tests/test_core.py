import pytest

from calculator.core import add, subtract, divide, power


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6


def test_divide():
    assert divide(9, 3) == 3


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(1, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1
    assert power(4, 0.5) == 2