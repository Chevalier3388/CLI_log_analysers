from .base_output import OutputInterface


class FileOutput(OutputInterface):
    """
    Класс реализующий вывод в файл.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def output(self, data: str) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(data)
