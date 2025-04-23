from data_outputs.console_output import ConsoleOutput


# Тест для проверки вывода
# Тест для проверки вывода
def test_console_output(capsys):
    # Создаем экземпляр класса ConsoleOutput
    console = ConsoleOutput()

    # Ожидаемый текст
    text = "Hello Pytest"

    # Вызываем метод output
    console.output(text)

    # Захватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что вывод соответствует ожидаемому
    assert (
        captured.out.strip() == text
    ), f"Ожидался вывод: '{text}', но получено: '{captured.out.strip()}'"
