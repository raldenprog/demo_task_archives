"""Содержит релизацию zip парсера архива"""
from typing import Any, List
from zipfile import ZipFile
from file_parsers import FileParserInterface

from .interface import ArchiveParserInterface


class ZipParser(ArchiveParserInterface):
    """Реализация zip парсера архива"""

    def parse_archive(self, file_parser: FileParserInterface, path: str) -> List[Any]:
        """
        Парсит zip файл с помощью file_parser

        Args:
            file_parser: файл парсер
            path: абсолютный путь до архива

        Returns:

        """
        result = []
        with ZipFile(path, 'r') as archive:
            for file_name in archive.namelist():
                with archive.open(file_name, 'r') as file:
                    result.append(file_parser.parse_file(file))
        return result
