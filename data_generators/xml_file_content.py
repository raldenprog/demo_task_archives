"""Содержит реализацию генерации содержимого xml"""
from lxml import etree

from .interface import FileContentInterface, IDGeneratorInterface, LevelGeneratorInterface, ObjectsGeneratorInterface


class SomeXmlFileContent(FileContentInterface):
    """Реализация генерации содержимого xml"""

    def __init__(
            self,
            name: str,
            id_gen: IDGeneratorInterface,
            level_gen: LevelGeneratorInterface,
            objects_gen: ObjectsGeneratorInterface,
    ) -> None:
        """
        Конструктор

        Args:
            name: название файла
            id_gen: объект реализующий интерфейс IDGeneratorInterface
            level_gen: объект реализующий интерфейс LevelGeneratorInterface
            objects_gen: объект ObjectsGeneratorInterface интерфейс LevelGeneratorInterface
        """
        self._id_gen = id_gen
        self._level_gen = level_gen
        self._objects_gen = objects_gen
        self._name = name

    def get_name(self) -> str:
        """Получить имя файла"""
        return f'{self._name}.xml'

    def get_file_content(self) -> str:
        """Получить содержимое файла"""
        root = etree.Element('root')
        var = etree.SubElement(root, 'var')
        var.attrib['name'] = 'id'
        var.attrib['value'] = self._id_gen.get_id()
        var = etree.SubElement(root, 'var')
        var.attrib['name'] = 'level'
        var.attrib['value'] = str(self._level_gen.get_level())
        objects = etree.SubElement(root, 'objects')
        for item in self._objects_gen.get_objects():
            etree.SubElement(objects, 'object').attrib['name'] = str(item)
        return etree.tostring(root, encoding='unicode')
