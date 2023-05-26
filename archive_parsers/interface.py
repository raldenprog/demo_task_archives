"""Содержит интерфейсы для парсинга архивов"""

from abc import ABC, abstractmethod
from file_parsers import FileParserInterface


class ArchiveParserInterface(ABC):
    """Интерфейс для парсинга архива"""

    @abstractmethod
    def parse_archive(self, file_parser: FileParserInterface, path: str) -> any:
        """
        С помощью переданного файл парасера должен распарсить архив по указанному пути

        Args:
            file_parser: объект файл парсера
            path: путь до архива

        Returns:
            Any
        """
