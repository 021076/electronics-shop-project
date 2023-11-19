import csv


class Item:
    """ Класс для представления товара в магазине."""

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return str(self.name)

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> float:
        """Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname):
        self.__name = newname[:10]

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        cls.all.clear()
        with open(csv_file, encoding='windows-1251', ) as f:
            reader = csv.DictReader(f)
            for row_csv in reader:
                item_list = list(row_csv.values())
                name, price, quantity = item_list
                price = float(price)
                quantity = cls.string_to_number(quantity)
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(from_str):
        return int(float(from_str))

    def __add__(self, other):
        """Метод для операции сложения"""
        return self.quantity + other.quantity
