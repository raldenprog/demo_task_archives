"""Содержит интерфейсы генераторов данных"""
from abc import ABC, abstractmethod
from typing import List


class IDGeneratorInterface(ABC):
    """Интерфейс генератора id"""

    @abstractmethod
    def get_id(self) -> str:
        """Генерирует id"""


class LevelGeneratorInterface(ABC):
    """Интерфейс генератора level"""

    @abstractmethod
    def get_level(self) -> int:
        """Генерирует level"""


class ObjectsGeneratorInterface(ABC):
    """Интерфейс генератора объектов"""

    @abstractmethod
    def get_objects(self) -> List[str]:
        """Генерирует objects"""


class FileContentInterface(ABC):
    """Интерфейс с данными файла"""

    @abstractmethod
    def get_name(self) -> str:
        """Получить название файла"""

    @abstractmethod
    def get_file_content(self) -> str:
        """Получить содержимое файла"""


class ArchiveGeneratorInterface(ABC):
    """Интерфейс генератора архива"""

    @abstractmethod
    def save_data(self, file_contents: List[FileContentInterface]) -> None:
        """Сохраняет данные в архив"""
