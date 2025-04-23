# main.py

import argparse
import os
import sys

from parsers.text_parser import TextParser
from reports.handlers_report import ReportLogEndpoint
from representations.info_table_perfomance import ViewTable
from data_outputs.console_output import ConsoleOutput


AVAILABLE_REPORTS = {"handlers": ReportLogEndpoint}


def main():
    parser = argparse.ArgumentParser(description="Анализ логов Django-приложения.")
    parser.add_argument("logfiles", nargs="+", help="Пути к логам (один или несколько)")
    parser.add_argument(
        "--report",
        choices=AVAILABLE_REPORTS.keys(),
        required=True,
        help="Тип отчёта (например, handlers)",
    )

    args = parser.parse_args()

    # Проверка файлов
    for file in args.logfiles:
        if not os.path.exists(file):
            print(f"Файл не найден: {file}")
            sys.exit(1)

    # Получение отчета
    report_class = AVAILABLE_REPORTS[args.report]
    report = report_class(TextParser())

    extracted_data = report.extract_data(args.logfiles)
    rendered_table = report.generate(ViewTable(), extracted_data)
    report.data_output(ConsoleOutput(), rendered_table)


if __name__ == "__main__":
    main()
