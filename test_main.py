import pytest
from main import Calculator, process_numbers


def test_add():
    calc = Calculator()
    assert calc.add(10, 5) == 15
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

    # test division by zero
    with pytest.raises(ValueError):
        calc.divide(5, 0)


def test_process_numbers():
    # normal case
    assert process_numbers([1, 2, 3, 4, 5, 6]) == 12

    # only odd numbers
    assert process_numbers([1, 3, 5]) == 0

    # empty list
    assert process_numbers([]) == 0

    # negative even numbers
    assert process_numbers([-2, -4, 3]) == -6
