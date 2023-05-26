"""Содержит реализацию генератора данных"""
from random import randint
from typing import List
from uuid import uuid4

from .interface import IDGeneratorInterface, ObjectsGeneratorInterface, LevelGeneratorInterface


class SomeDataGenerator(
    IDGeneratorInterface,
    ObjectsGeneratorInterface,
    LevelGeneratorInterface,
):
    """Генератор данных"""

    def get_id(self) -> str:
        """Генерирует id"""
        return uuid4().hex

    def get_level(self) -> int:
        """Генерирует level"""
        return randint(1, 100)

    def get_objects(self) -> List[str]:
        """Генерирует objects"""
        return [uuid4().hex for _ in range(randint(1, 10))]
