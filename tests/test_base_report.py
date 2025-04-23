from typing import List, Dict

import pytest
from reports.base_report import ReportInterface
from representations.base_performance import ViewInterface
from data_outputs.base_output import OutputInterface
from parsers.text_parser import TextParser


class TestClass(ReportInterface):
    def extract_data(self, file_path: List) -> Dict:
        pass

    def generate(self, method_view: ViewInterface, data: Dict):
        pass

    def data_output(self, method_output: OutputInterface, data: str):
        pass


# Функция теста для проверки, что объект является экземпляром ReportInterface
def test_is_instance_of_report_interface():
    p = TextParser()
    t_class = TestClass(p)

    # Проверяем, что t_class является экземпляром ReportInterface
    assert isinstance(
        t_class, ReportInterface
    ), f"TestClass не является экземпляром ReportInterface"


# Функция теста для проверки, что TestClass является подклассом ReportInterface
def test_is_subclass_of_report_interface():
    # Проверяем, что TestClass является подклассом ReportInterface
    assert issubclass(
        TestClass, ReportInterface
    ), f"TestClass не является подклассом ReportInterface"
