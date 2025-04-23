import os
import tempfile
import sys
import pytest
from main import main


def test_main_with_temp_file(monkeypatch):
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmpfile:
        tmpfile.write(
            "2025-04-23 00:00:00 INFO django.request: GET /api/ 200 OK [127.0.0.1]"
        )
        tmpfile_name = tmpfile.name

    monkeypatch.setattr(sys, "argv", ["main.py", tmpfile_name, "--report", "handlers"])

    try:
        main()
    except SystemExit:
        pass  # main может вызвать exit(), мы игнорируем это

    os.remove(tmpfile_name)
