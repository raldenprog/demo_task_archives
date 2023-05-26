"""Модуль содержит реализации и интерфейсы для парсинга архивов"""

from .interface import ArchiveParserInterface
from .zip import ZipParser

__all__ = [
    'ArchiveParserInterface',
    'ZipParser',
]

