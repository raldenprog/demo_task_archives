"""
Содержит реализацию задания 1

1. Создает 50 zip-архивов, в каждом 100 xml файлов со случайными данными следующей структуры:
<root>
<var name=’id’ value=’<случайное уникальное строковое значение>’/>
<var name=’level’ value=’<случайное число от 1 до 100>’/>
<objects>
<object name=’<случайное строковое значение>’/>
<object name=’<случайное строковое значение>’/>
…
</objects>
</root>
В тэге objects случайное число (от 1 до 10) вложенных тэгов object.
"""
import os

from data_generators import SomeDataGenerator, SomeXmlFileContent, ZipGenerator


def do_task_first(path: str, qty_archives: int = 50, qty_xml: int = 100):
    """
    Выполнить задание 1

    Args:
        path: абсолютный путь до папки с zip архивами
        qty_archives: количество создаваемых архивов
        qty_xml: количество xml в одном архиве
    """
    data_gen = SomeDataGenerator()
    for archive_number in range(qty_archives):
        ZipGenerator(str(archive_number), path).save_data(
            [SomeXmlFileContent(str(i), data_gen, data_gen, data_gen) for i in range(qty_xml)]
        )


if __name__ == '__main__':
    do_task_first(f'{os.getcwd()}/folder_for_files/zip')
