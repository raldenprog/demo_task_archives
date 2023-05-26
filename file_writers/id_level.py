"""Содержит реализацию для записи CSV файла с id и level"""
import csv
import os
from typing import Tuple

from .interface import FileWriterInterface


class IdLevelCSVWriter(FileWriterInterface):
    """Реализация для записи CSV файла с id и level"""

    def __init__(self, path: str, file_name: str) -> None:
        """
        Конструктор

        Args:
            path: абсолютный путь до папки, куда сохранить новый файл или дописать существующий
            file_name: имя файла
        """
        self._path = path
        self._file_name = file_name

    def write(self, data: Tuple[str, str]) -> None:
        """
        Запись данных в csv файл. Если такой файл уже существует, то он будет дописан в конец.

        Args:
            data: данные с id и level
        """
        with open(os.path.join(self._path, f'{self._file_name}.csv'), 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
