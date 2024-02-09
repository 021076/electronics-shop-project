"""Набор фикстур для тестов"""
import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard


@pytest.fixture
def some_item():
    return Item("Товар", 5000, 50)


@pytest.fixture
def some_phone():
    return Phone("Смартфон", 15000, 4, 2)


@pytest.fixture
def some_keyboard():
    return Keyboard("Keyboard XV-8", 2750, 31)
