from unittest.mock import Mock

import pytest
from Tasks import Tasks


def test_find_average():
    assert Tasks.find_average([1, 2, 3, 4, 5]) == 3


def test_not_a_list():
    with pytest.raises(TypeError):
        Tasks.find_average("It is not a list")


def test_transfer_money():
    person = Tasks.Person(1000)
    bank = Tasks.Bank()
    person.transfer_money(900, bank)
    assert person.balance == 100
    assert bank.balance == 900


def test_mock_transfer():
    person = Tasks.Person(1000)
    bank_mock = Mock()
    person.transfer_money(900, bank_mock)
    assert person.balance == 100
    bank_mock.receive_money.assert_called_with(900)


def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Tasks.divide(100, 0)


@pytest.mark.parametrize("a, b, expected", [
    (10, 0, 0), (2, 3, 6), (10, 1, 10)])
def test_multiply(a, b, expected):
    assert Tasks.multiply(a, b) == expected


@pytest.mark.parametrize("a, expected", [
    (4, False), (5, True), (8, False)])
def test_simple(a, expected):
    assert Tasks.is_prime(a) == expected
