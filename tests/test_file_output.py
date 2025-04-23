import os
import pytest
from data_outputs.file_output import FileOutput


# Проверка создания объекта с правильным путем
def test_file_output_creation():
    file_path = "test_output.txt"
    file_output = FileOutput(file_path)

    # Проверяем, что объект создан с правильным атрибутом пути
    assert file_output.file_path == file_path


def test_output_to_file(tmp_path):
    # Используем временный файл, создаваемый pytest с помощью tmp_path
    file_path = tmp_path / "test_output.txt"
    file_output = FileOutput(str(file_path))

    # Данные, которые будем записывать в файл
    data = "Hello, this is a test."

    # Вызываем метод output
    file_output.output(data)

    # Проверяем, что данные записались в файл
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    assert content == data
