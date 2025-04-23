from .base_output import OutputInterface


class ConsoleOutput(OutputInterface):
    """
    Класс реализующий вывод в консоль.
    """

    def output(self, data: str):
        print(data)  # Выводим данные в консоль
