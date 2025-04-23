from abc import ABC, abstractmethod
from typing import Dict


class ViewInterface(ABC):
    """
    Базовый класс выводов
    """

    @abstractmethod
    def render(self, data: Dict) -> None:
        """
        Метод для представления данных.
        """
        pass
