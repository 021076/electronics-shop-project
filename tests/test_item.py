"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def some_item():
    return Item("Товар", 5000, 50)


def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 250000


def test_apply_discount(some_item):
    some_item.pay_rate = 0.5
    some_item.apply_discount()
    assert some_item.price == 2500.0


def test_name(some_item):
    some_item.name = 'Смартфон'
    assert some_item.name == 'Смартфон'
    with pytest.raises(Exception):
        some_item.name = 'СуперСмартфон'


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
