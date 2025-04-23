from abc import ABC, abstractmethod


class OutputInterface(ABC):
    """
    Базовый класс выводов
    """

    @abstractmethod
    def output(self, data: str) -> None:
        """
        Метод для вывода данных.
        """
        pass
