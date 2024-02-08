from src.item import Item


class Phone(Item):
    """Дочерний класс телефонов, наследуется от класса Item.
                    :param name: Название товара.
                    :param price: Цена за единицу товара.
                    :param quantity: Количество товара в магазине.
                    :number_of_sim: Количество SIM-карт.
                    """

    def __init__(self, name, price, quantity, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim: int):
        self._number_of_sim = new_number_of_sim
        # if new_number_of_sim == 0:
        if new_number_of_sim <= 0 or new_number_of_sim % 1 != 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
