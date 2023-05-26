"""Модуль содержит реализации и интерфейсы файл парсеров"""

from .interface import FileParserInterface
from .id_level import IdLevelParser
from .id_objects import IdObjectNameParser

__all__ = [
    'FileParserInterface',
    'IdLevelParser',
    'IdObjectNameParser',
]
