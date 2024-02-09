"""Здесь надо написать тесты с использованием pytest для модуля Keyboard."""
import pytest
from src.keyboard import Keyboard


def test__repr__(some_keyboard):
    assert some_keyboard.__repr__() == "Keyboard('Keyboard XV-8', 2750, 31)"


def test__str__(some_keyboard):
    assert some_keyboard.__str__() == 'Keyboard XV-8'
    assert str(some_keyboard.language) == "EN"


def test_change_lang(some_keyboard):
    assert str(some_keyboard.language) == "EN"
    some_keyboard.change_lang()
    assert str(some_keyboard.language) == "RU"
    some_keyboard.change_lang()
    assert str(some_keyboard.language) == "EN"


def test_language(some_keyboard):
    with pytest.raises(AttributeError):
        some_keyboard.language = 'РУ'
