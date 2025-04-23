from collections import defaultdict
from typing import Dict

from representations.base_performance import ViewInterface


class ViewTable(ViewInterface):
    """
    Класс для отображения данных в виде таблицы.
    """

    def render(self, data: Dict) -> str:
        """
        Формирует строковое представление данных в виде таблицы.
        """
        # Собираем все уникальные уровни логирования
        levels = sorted({lvl for endpoint in data.values() for lvl in endpoint.keys()})
        headers = ["ENDPOINT"] + levels

        table = [headers]

        totals = defaultdict(int)  # для подсчета итоговых значений

        for endpoint, level_counts in data.items():
            row = [endpoint] + [str(level_counts.get(level, 0)) for level in levels]
            table.append(row)
            for i, level in enumerate(levels):
                totals[level] += int(
                    row[i + 1]
                )  # суммируем по каждому уровню логирования

        # Форматируем таблицу в строку
        col_widths = [max(len(str(cell)) for cell in col) for col in zip(*table)]
        formatted_rows = []
        for row in table:
            formatted_row = "  ".join(
                str(cell).ljust(width) for cell, width in zip(row, col_widths)
            )
            formatted_rows.append(formatted_row)

        # Добавляем итоговую строку
        total_line = "TOTAL"
        for level in sorted(totals.keys()):
            total_line += f"  {totals[level]}"

        formatted_rows.append(total_line)
        formatted_rows.insert(
            0, f"Total requests: {sum(totals.values())}"
        )  # Строка с общим количеством реквестов

        return "\n".join(formatted_rows)
