"""Содержит реализацию генератора zip архива"""
import os
from typing import List
from zipfile import ZipFile

from .interface import ArchiveGeneratorInterface, FileContentInterface


class ZipGenerator(ArchiveGeneratorInterface):
    """Реализация генератора zip архива"""

    def __init__(self, name: str, path: str):
        """
        Конструктор

        Args:
            name: название архива
            path: абсолютный путь до директории, где сохранить архив
        """
        self._name = name
        self._path = path

    def save_data(self, file_contents: List[FileContentInterface]) -> None:
        """
        Сохраняет данные в архив. Если архив есть, перезаписывает его

        Args:
            file_contents: объект реализующий интерфейс FileContentInterface
        """
        with ZipFile(os.path.join(self._path, f'{self._name}.zip'), 'w') as archive:
            for content in file_contents:
                archive.writestr(content.get_name(), content.get_file_content())
