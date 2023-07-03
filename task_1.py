# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
#
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
#
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

import os


def split_file_path(file_path):
    """Функция для отделения пути, имени файла и его расширения"""
    file_dir, file_name = os.path.split(file_path)

    file_name, file_extension = os.path.splitext(file_name)

    return file_dir, file_name, file_extension


file_path = "c:/Users/Vladislav/Desktop/deep_to_python/test.txt"
result = split_file_path(file_path)
print(result)
