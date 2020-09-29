'''Tests for calculator module.'''

import pytest

import source.calculator as calc


# Addition
def test_add_two_numbers():
    assert calc.add(4, 5) == 9


def test_add_many_numbers():
    assert calc.add(*range(100)) == 4950


# Subtraction
@pytest.mark.parametrize(
    'actual, expected',
    [
        ((9.6, 3.4), 6.2),
        ((-7.5, -2.6), -4.9),
        ((0, 0), 0),
    ])
def test_sub(actual, expected):
    '''Test corner cases of sub function'''
    assert calc.sub(*actual) == pytest.approx(expected)


# Multiplication
@pytest.mark.parametrize(
    'actual, expected',
    [
        ((2.5, 6.3), 15.75),
        ((-3.1, -5.7), 17.67),
        (range(1, 10), 362_880),
    ])
def test_mul(actual, expected):
    '''Test "corner cases" of mul function'''
    assert calc.mul(*actual) == pytest.approx(expected)


def test_multiply_by_zero_exception():
    with pytest.raises(ValueError):
        calc.mul(1, 0)


# Division
@pytest.mark.parametrize(
    'actual, expected',
    [
        ((1, 3), 0.333),
        ((-9, -3), 3),
        ((-1, 0), -float('inf')),
    ])
def test_div(actual, expected):
    '''Test "corner cases" of mul function'''
    assert calc.div(*actual) == pytest.approx(expected, abs=0.001)


# Averaging
def test_average_list():
    assert calc.avg([2, 5, 12, 98]) == 29.25


def test_average_range():
    assert calc.avg(range(19)) == 9


def test_average_outliers():
    assert calc.avg(
        [2, 5, 12, 98],
        lower_bound=0,
        upper_bound=50
    ) == pytest.approx(6.333, rel=0.01)


def test_average_zero_limit():
    assert calc.avg([-1, 0, 1], lower_bound=0) == 0.5


def test_average_empty_iterable():
    with pytest.raises(ZeroDivisionError):
        calc.avg([])


def test_average_non_iterable():
    with pytest.raises(TypeError):
        calc.avg(123)
