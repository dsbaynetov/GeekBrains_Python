'''

Функции работы с файлами
'''
import os
import shutil

#создание файла
from typing import List, Any


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

#создать папку
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print('Папка уже существует')

#удалить файл/папку
def delete_file(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except TypeError as e:
        print(f'Ошибка параметров {e}')
    except FileNotFoundError as e2:
        print(f'Не удается найти указанный файл или папку: {name}, {e2}')


#получить список файлов и/или папок
def file_list(file_path, folders_only=False):
    result = os.listdir(file_path)
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def copy_file(source, target):
    try:
        if os.path.isdir(source):
            shutil.copytree(source, target)
        else:
            shutil.copy(source, target)
    except FileExistsError:
        print('Папка или файл с таким именем уже существует')
    except FileNotFoundError as e2:
        print('Файл с именем {} не найден. {}'.format(source, e2))
    except Exception:
        print(f'Ошибка копирования файла или папки. {e3}')



#сменить текущий каталог
def change_dir(dest):
    try:
        os.chdir(dest)
        print(f'Каталог успешно изменен. Текущий каталог {os.getcwd()}')
    except FileNotFoundError as e1:
        print(f'Каталог {dest} не найден. {e1} ')

