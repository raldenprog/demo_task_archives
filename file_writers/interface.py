"""Содержит интерфейсы для записи файлов"""

from abc import ABC, abstractmethod


class FileWriterInterface(ABC):
    """Интерфейс для записи файла"""

    @abstractmethod
    def write(self, data) -> None:
        """
        Должен принять на вход данные и записать в файл

        Args:
            data: какие-то данные
        """
