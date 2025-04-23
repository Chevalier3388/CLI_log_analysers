from abc import abstractmethod, ABC
from typing import List, Dict

from data_outputs.base_output import OutputInterface
from parsers.base_parser import ParserInterface
from representations.base_performance import ViewInterface


class ReportInterface(ABC):
    """
    Базовый класс отчётов.
    """

    def __init__(self, parser: ParserInterface):
        self.parser = parser

    @abstractmethod
    def extract_data(self, file_path: List) -> Dict:
        """
        Парсит логи, используя переданный парсер.
        Собирает нужные нам данные.
        """
        data = self.parser.parse(file_path)
        return data

    @abstractmethod
    def generate(self, method_view: ViewInterface, data: Dict):
        """
        Метод для формирования отчёта.
        """
        pass

    @abstractmethod
    def data_output(self, method_output: OutputInterface, data: str):
        """
        Выводит результаты анализа.
        """
        pass
