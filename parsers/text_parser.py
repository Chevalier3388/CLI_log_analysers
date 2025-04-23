import os
import re
from parsers.base_parser import ParserInterface


class TextParser(ParserInterface):
    """
    Парсер логов Django в текстовом формате.
    """

    REQUEST_PATTERN = re.compile(
        r'(?P<level>DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+django\.request:.*?(?P<endpoint>/[^\s"]+)/'
    )

    def parse(self, file_paths: list):
        for path in file_paths:
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    match = self.REQUEST_PATTERN.search(line)
                    if match:
                        yield {
                            "level": match.group("level"),
                            "endpoint": match.group("endpoint") + "/",
                        }


# p = TextParser()
# gen = p.parse(["../logs/app1.log", "../logs/app2.log"])
#
# for i, _ in enumerate(gen):
#     print(i, _)
