import pytest
from representations.info_table_perfomance import (
    ViewTable,
)  # Замените на правильный путь импорта ViewTable


# Фикстура, которая предоставляет данные для теста
@pytest.fixture
def log_data():
    return {
        "/api/v1/reviews/": {"CRITICAL": 2, "ERROR": 1, "INFO": 11},
        "/admin/dashboard/": {"CRITICAL": 0, "ERROR": 3, "INFO": 10},
    }


# Тест на генерацию отчета
def test_generate_report(log_data):
    # Создаём экземпляр ViewTable
    view = ViewTable()

    # Генерируем отчёт
    report_data = view.render(log_data)

    # Ожидаемый вывод с подгонкой данных
    expected_report = """Total requests: 27
ENDPOINT           CRITICAL  ERROR  INFO
/api/v1/reviews/   2         1      11  
/admin/dashboard/  0         3      10  
TOTAL  2  4  21"""

    # Убираем лишние пустые строки и пробелы, чтобы избежать ошибок
    assert report_data.strip() == expected_report.strip()
