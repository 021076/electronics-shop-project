from src.item import Item
from src.mixins import MixinLanguage


class Keyboard(Item, MixinLanguage):
    """Дочерний класс клавиатур, наследуется от класса Item c подмешиванием миксина языковой раскладки"""

    def __init__(self, name, price, quantity) -> None:
        super().__init__(name, price, quantity)
