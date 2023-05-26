"""Содержит реализацию для записи CSV файла с id и object name"""
import csv
import os
from typing import List, Tuple

from .interface import FileWriterInterface


class IdObjectNameCSVWriter(FileWriterInterface):
    """Реализация для записи CSV файла с id и object name"""

    def __init__(self, path: str, file_name: str) -> None:
        """
        Конструктор

        Args:
            path: абсолютный путь до папки, куда сохранить новый файл или дописать существующий
            file_name: имя файла
        """
        self._path = path
        self._file_name = file_name

    def write(self, data: List[Tuple[str, str]]) -> None:
        """
        Запись данных в csv файл. Если такой файл уже существует, то он будет дописан в конец.

        Args:
            data: данные с id и object name
        """
        with open(os.path.join(self._path, f'{self._file_name}.csv'), 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for d in data:
                writer.writerows(d)
