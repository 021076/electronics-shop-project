"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 250000


def test_apply_discount(some_item):
    Item.pay_rate = 0.8
    assert some_item.apply_discount() == 4000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[1].price == 1000.0
    assert Item.all[2].quantity == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test__repr__(some_item):
    assert some_item.__repr__() == "Item('Товар', 5000, 50)"


def test__str__(some_item):
    assert some_item.__str__() == 'Товар'

def test__add__():
    item1=Item('Товар1', 15000, 17)
    item2 = Item('Товар2', 25000, 21)
    assert item1.quantity + item2.quantity == 38