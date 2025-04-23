# tests/test_parser.py

from parsers.text_parser import TextParser

log_content = """
2025-03-28 12:05:13,000 INFO django.request: GET /api/v1/reviews/ 201 OK [192.168.1.97]
2025-03-28 12:11:57,000 ERROR django.request: Internal Server Error: /admin/dashboard/ [192.168.1.29] - ValueError: Invalid input data
2025-03-28 12:37:43,000 INFO django.request: GET /api/v1/users/ 204 OK [192.168.1.36]
2025-03-28 12:09:16,000 INFO django.request: GET /api/v1/cart/ 204 OK [192.168.1.93]
2025-03-28 12:04:09,000 INFO django.request: GET /api/v1/products/ 204 OK [192.168.1.44]
2025-03-28 12:25:37,000 ERROR django.request: GET /api/v1/support/ 204 OK [192.168.1.35]
"""


def test_parser_parses_correctly(tmp_path):
    log_file = tmp_path / "test.log"
    log_file.write_text(log_content)

    parser = TextParser()
    parsed = list(parser.parse([str(log_file)]))  # преобразуем генератор в список

    assert len(parsed) == 6
    assert parsed[0]["level"] == "INFO"
    assert parsed[-1]["level"] == "ERROR"
    assert parsed[2]["endpoint"] == "/api/v1/users/"
