class MixinLanguage:
    """Класс-миксин для хранения и изменения раскладки клавиатуры"""

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    @property
    def language(self):
        return self.__language
