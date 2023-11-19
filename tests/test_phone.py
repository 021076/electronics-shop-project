"""Здесь надо написать тесты с использованием pytest для модуля Phone."""
from src.phone import Phone


def test__repr__(some_phone):
    assert some_phone.__repr__() == "Phone('Смартфон', 15000, 4, 2)"


def test__str__(some_phone):
    assert some_phone.__str__() == 'Смартфон'


def test__add__(some_phone, some_item):
    assert some_phone.quantity + some_item.quantity == 54
    phone1 = Phone('Samsung A8+', 15000, 11, 1)
    phone2 = Phone('TECHNO CAMON 19 Pro', 25000, 1, 2)
    assert phone1.quantity + phone2.quantity == 12


