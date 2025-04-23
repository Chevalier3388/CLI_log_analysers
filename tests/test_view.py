import pytest
from representations.info_table_perfomance import ViewTable


# Фикстура, которая предоставляет данные для теста
@pytest.fixture
def log_data():
    return {
        "/api/v1/reviews/": {"CRITICAL": 2, "ERROR": 1, "INFO": 11},
        "/admin/dashboard/": {"CRITICAL": 0, "ERROR": 3, "INFO": 10},
    }


# Тест на рендеринг данных
def test_render_method(log_data):
    view = ViewTable()

    # Проверяем, что метод render() возвращает ожидаемый результат
    rendered_data = view.render(log_data)
    assert isinstance(rendered_data, str), "Метод render должен возвращать строку"


# Тест на правильность подсчета данных
def test_count_requests(log_data):
    view = ViewTable()

    # Получаем данные из метода render
    rendered_data = view.render(log_data)

    # Извлекаем число запросов из строки, возвращаемой методом render
    total_requests_line = rendered_data.splitlines()[0]
    total_requests = int(total_requests_line.split(":")[1].strip())

    # Проверяем, что общее количество запросов равно 27
    assert total_requests == 27
