# CLI Log Analyser

Утилита командной строки для анализа логов Django-приложения.  
Позволяет собирать и выводить отчёты по обработанным логам в различных форматах.

Установка:
git clone https://github.com/Chevalier3388/cli-log-analyser.git
cd cli-log-analyser
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Запуск:
python main.py path/to/logfile.log --report handlers

Для запуска с отображением покрытия:
pytest --cov=. tests/

Пример лог-файла:
2025-04-23 00:00:00 INFO django.request: GET /api/v1/users/ 200 OK [127.0.0.1]

Ссылка на репозиторий:
https://github.com/Chevalier3388/CLI_log_analysers
