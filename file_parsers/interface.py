"""Содержит интерфейсы для парсинга файлов"""
from abc import ABC, abstractmethod
from typing import IO


class FileParserInterface(ABC):
    """Интерфейс для парсинга файла"""

    @abstractmethod
    def parse_file(self, file: IO) -> any:
        """
        Метод должен принять на вход IO и выдать в ответ какие-то данные

        Args:
            file: io файла

        Returns:
            Any
        """
