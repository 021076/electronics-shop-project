from src.item import Item


class Phone(Item):
    """Дочерний класс телефонов, наследуется от класса Item"""

    # number_of_sim > 0
    def __init__(self, name, price, quantity, number_of_sim: int) -> None:
        """Создание экземпляра класса Phone.
                :param name: Название товара.
                :param price: Цена за единицу товара.
                :param quantity: Количество товара в магазине.
                :number_of_sim: Количество SIM-карт.
                """
        super().__init__(name, price, quantity)
        try:
            self.number_of_sim = number_of_sim  # raw_input in Python 2.x
            if self.number_of_sim == 0:
                raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        except ValueError as e:
            print(e)
        # if number_of_sim == 0:
        #     raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        # super().__init__(name, price, quantity)
        # try:
        #     number_of_sim == 0
        # except ValueError:
        #     print("Количество физических SIM-карт должно быть целым числом больше нуля.")
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
        # try:
        #     number_of_sim == 0
        # except ValueError:
        #     print("Количество физических SIM-карт должно быть целым числом больше нуля.")
        # else:
        #     super().__init__(name, price, quantity)
        #     self.number_of_sim = number_of_sim
        #
        # if number_of_sim > 0:
        #     super().__init__(name, price, quantity)
        #     self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """Метод для операции сложения только между классами Phone и Item"""
        if other.__class__ == self.__class__ or other.__class__ == Item:
            return self.quantity + other.quantity

    # def sim_not_zero(self, number_of_sim):
    #     try:
    #         self.number_of_sim == 0
    #     except ValueError:
    #         print("Количество физических SIM-карт должно быть целым числом больше нуля.")
    #     else:
    #         return self.number_of_sim
