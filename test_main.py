import pytest
from src.main import Calculator, process_numbers   # change 'app' to your filename


def test_add():
    calc = Calculator()
    assert calc.add(10, 20) == 30
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0


def test_divide():
    calc = Calculator()
    assert calc.divide(50, 5) == 10
    assert calc.divide(9, 3) == 3


def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)


def test_process_numbers_normal():
    assert process_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert process_numbers([2, 4, 6, 8]) == 20
    assert process_numbers([1, 3, 5]) == 0


def test_process_numbers_empty():
    assert process_numbers([]) == 0
