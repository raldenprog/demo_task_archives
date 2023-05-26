"""Содержит реализацию файл парсера значений id, object"""
from typing import IO, List, Tuple
from lxml import etree

from .interface import FileParserInterface


class IdObjectNameParser(FileParserInterface):
    """Файл парсер значений id, object из xml"""

    def parse_file(self, file: IO) -> List[Tuple[str, str]]:
        """
        Читает из файла значения id и object

        Args:
            file: io файл

        Returns:
            id, object в виде массива
        """
        tree = etree.parse(file)
        id_ = tree.xpath('/root/var[@name="id"]')[0].attrib['value']
        id_object_name = []
        objects = tree.xpath('/root/objects/object')
        for object_ in objects:
            id_object_name.append((id_, object_.attrib['name']))
        return id_object_name
