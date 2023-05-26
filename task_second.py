"""
Содержит реализацию задания 2

2. Обрабатывает директорию с полученными zip архивами, разбирает вложенные xml файлы и формирует 2 csv файла:
Первый: id, level - по одной строке на каждый xml файл
Второй: id, object_name - по отдельной строке для каждого тэга object (получится от 1 до 10 строк на каждый xml файл)
Очень желательно сделать так, чтобы задание 2 эффективно использовало ресурсы многоядерного процессора.
Порядок записей не важен

"""
import multiprocessing
import os
from typing import List, Tuple

from archive_parsers import ZipParser
from file_parsers import FileParserInterface, IdLevelParser, IdObjectNameParser
from file_writers import FileWriterInterface, IdLevelCSVWriter, IdObjectNameCSVWriter


def find_zip_in_path(path: str) -> List[str]:
    """
    Найти zip архивы в папке

    Args:
        path: абсолютный путь до директории с zip архивами

    Returns:
        абсолютные пути до всех zip архивов
    """
    archive_paths = []
    for filename in os.listdir(path):
        if filename.endswith('.zip'):
            archive_paths.append(os.path.join(path, filename))
    return archive_paths


def parse_zips(path_to_zip, file_parsers_and_writers: List[Tuple[FileParserInterface, FileWriterInterface]]) -> None:
    """
    Метод парсит zip архивы с помощью FileParser и создает по их данным файлы с помощью FileWriter

    Args:
        path_to_zip: абсолютные пути до zip архивов
        file_parsers_and_writers:
            0 элемент tuple - это FileParser
            1 элемент tuple - это FileWriter

    Returns:
        None
    """
    with multiprocessing.Pool() as pool:
        zip_parser = ZipParser()
        async_results = []

        # Запуск FileParser
        for parser, _ in file_parsers_and_writers:
            parser_results = []
            for path in find_zip_in_path(path_to_zip):
                parser_results.append(pool.apply_async(zip_parser.parse_archive, (parser, path)))
            async_results.append(parser_results)

        # Запуск FileWriter
        for i, parser_results in enumerate(async_results):
            writer = file_parsers_and_writers[i][1]
            for result in parser_results:
                writer.write(result.get())


def do_task_second(path_to_zip, path_to_csv) -> None:
    """
    Выполнить задание 2

    Args:
        path_to_zip: абсолютный путь до папки с zip архивами
        path_to_csv: абсолютный путь до папки куда сохранить csv
    """
    parse_zips(path_to_zip, [
        (IdLevelParser(), IdLevelCSVWriter(path_to_csv, '1_file')),
        (IdObjectNameParser(), IdObjectNameCSVWriter(path_to_csv, '2_file')),
    ])


if __name__ == '__main__':
    do_task_second(
        f'{os.getcwd()}/folder_for_files/zip',
        f'{os.getcwd()}/folder_for_files/csv'
    )
