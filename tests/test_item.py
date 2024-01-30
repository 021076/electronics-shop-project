"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def some_item():
    return Item("Товар", 5000, 50)


def test_calculate_total_price(some_item):
    assert some_item.calculate_total_price() == 250000


def test_apply_discount(some_item):
    """ Уточнение наставника: Вызов метода через класс, можно применить, если бы в apply_discount был бы return
    Скидка в данном случае применяется на все товары """
    # Item.pay_rate = 0.8
    # assert some_item.apply_discount() == 4000.0
    # вызов метода через экземпляр класса, применение скидки к конкретному товару
    some_item.pay_rate = 0.5
    some_item.apply_discount()
    assert some_item.price == 2500.0