"""Здесь надо написать тесты с использованием pytest для модуля Phone."""
import pytest

from src.phone import Phone
from src.item import Item


def test_issubclass():
    assert issubclass(Phone, Item) == True


def test_isinstance(some_item, some_phone):
    assert isinstance(some_phone, Phone) == True
    assert isinstance(some_item, Phone) == False


def test__repr__(some_phone):
    assert some_phone.__repr__() == "Phone('Смартфон', 15000, 4, 2)"


def test__str__(some_phone):
    assert some_phone.__str__() == 'Смартфон'


def test_number_of_sim(some_phone):
    some_phone.number_of_sim = 4
    assert some_phone.number_of_sim == 4
    with pytest.raises(ValueError):
        some_phone.number_of_sim = 0
        some_phone.number_of_sim = 1.1
        some_phone.number_of_sim = -5


def test__add___(some_phone, some_item):
    assert some_phone.quantity + some_phone.quantity == 8
    assert some_phone.quantity + some_item.quantity == 54
    # with pytest.raises(ValueError):
