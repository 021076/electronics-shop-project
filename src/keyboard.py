from src.item import Item, MixinLanguage

class Keyboard(Item, MixinLanguage):
    """Дочерний класс клавиатур, наследуется от класса Item c подмешиванием миксина языковой раскладки"""

    def __init__(self, name, price, quantity) -> None:
        super().__init__(name, price, quantity)

    # @property
    # def language(self):
    #     try:
    #         self.language == "RU" or self.language == "EN"
    #     except AttributeError as e:
    #         print(e)
    #     return self.language