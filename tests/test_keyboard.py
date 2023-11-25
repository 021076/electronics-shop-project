"""Здесь надо написать тесты с использованием pytest для модуля Keyboard."""

from src.keyboard import Keyboard

def test__repr__(some_keyboard):
    assert some_keyboard.__repr__() == "Keyboard('Keyboard XV-8', 2750, 31)"

def test__str__(some_keyboard):
    assert some_keyboard.__str__() == 'Keyboard XV-8'