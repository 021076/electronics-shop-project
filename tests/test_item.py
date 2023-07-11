"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def some_item():
    return Item("Товар", 5000, 50)

def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 250000

def test_apply_discount(some_item):
    Item.pay_rate = 0.8
    assert some_item.apply_discount() == 4000.0

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_init():
    item_10w = Item("Смартфон", 10000.50, 15)
    assert item_10w.name == "Смартфон"
    item_10w.name = "СуперСмартфон"
    assert item_10w.name == "СуперСмарт"