from typing import Dict, List
from collections import defaultdict

from .base_report import ReportInterface
from data_outputs.console_output import ConsoleOutput
from representations.info_table_perfomance import ViewTable
from parsers.text_parser import TextParser


class ReportLogEndpoint(ReportInterface):
    """
    Класс для формирования отчёта по эндпоинтам и уровням логирования.
    """

    def __init__(self, parser: TextParser):
        super().__init__(parser)

    def extract_data(self, file_path: list) -> Dict:
        """
        Парсит логи из файла и собирает данные только по указанным уровням логирования.
        """
        log_data = self.parser.parse(file_path)
        endpoint_stats = defaultdict(lambda: defaultdict(int))
        for entry in log_data:
            endpoint = entry.get("endpoint")
            level = entry.get("level")
            endpoint_stats[endpoint][level] += 1

        data_info = {ep: dict(levels) for ep, levels in endpoint_stats.items()}

        return data_info

    def generate(self, method_view: ViewTable, ex_data: Dict):
        """
        Метод для формирования отчёта.
        """

        report_data = method_view.render(ex_data)

        return report_data

    def data_output(self, method_output: ConsoleOutput, table_data: str):
        """
        Выводит результаты анализа.
        """
        method_output.output(table_data)
