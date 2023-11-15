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

