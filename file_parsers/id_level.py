"""Содержит реализацию файл парсера значений id, level"""
from typing import IO, Tuple
from lxml import etree

from .interface import FileParserInterface


class IdLevelParser(FileParserInterface):
    """Файл парсер значений id, level из xml"""

    def parse_file(self, file: IO) -> Tuple[str, str]:
        """
        Читает из файла значения id и level

        Args:
            file: io файл

        Returns:
            id, level
        """
        tree = etree.parse(file)
        return (
            tree.xpath('/root/var[@name="id"]')[0].attrib['value'],
            tree.xpath('/root/var[@name="level"]')[0].attrib['value'],
        )
