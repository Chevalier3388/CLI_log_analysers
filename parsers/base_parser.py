from abc import ABC, abstractmethod


class ParserInterface(ABC):
    """
    Базовый класс парсеров
    """

    @abstractmethod
    def parse(self, path: list):
        """
        Метод для парсинга данных
        """
        pass
