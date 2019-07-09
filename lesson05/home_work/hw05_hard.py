# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not src_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), src_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(src_name))
    except FileExistsError:
        print('директория {} уже существует'.format(src_name))


def ping():
    print("pong")


def copy_file():
    '''
    Копирование файла или каталога
    '''
    if (not src_name) or (not trg_name):
        print("Необходимо указать имя файла источника и приемника вторым и третьим параметром")
        return
    src_path=os.path.join(os.getcwd(), src_name)
    trg_path=os.path.join(os.getcwd(), trg_name)
    try:
        if os.path.isdir(src_path):
            shutil.copytree(src_path, trg_path)
        else:
            shutil.copy(src_path, trg_path)
        print(f'Файл/Каталог "{src_name}" успешно скопирован в "{trg_name}"')
    except FileExistsError:
        print('Папка или файл с таким именем уже существует')
    except FileNotFoundError as e2:
        print(f'Файл с именем {src_path} не найден. {e2}')
    except Exception as e3:
        print(f'Ошибка копирования файла или папки. {e3}')


def delete_file():
    if (not src_name):
        print("Необходимо указать имя файла/папки для удаления вторым параметром")
        return
    src_path=os.path.join(os.getcwd(), src_name)

    try:
        if os.path.isdir(src_path):
            os.rmdir(src_path)
        else:
            os.remove(src_path)
        print(f'Файл/Каталог "{src_name}" успешно удален')
    except TypeError as e:
        print(f'Ошибка параметров {e}')
    except FileNotFoundError as e2:
        print(f'Не удается найти указанный файл или папку: {src_path}, {e2}')

def change_dir():
    if (not src_name):
        print("Необходимо указать имя файла/папки для удаления вторым параметром")
        return

    try:
        os.chdir(src_name)
        print(f'Каталог успешно изменен. Текущий каталог {os.getcwd()}')
    except FileNotFoundError as e1:
        print(f'Каталог {src_name} не найден. {e1} ')

def file_list(folders_only=False):

    result = os.listdir(os.getcwd())
    print(f'\nТекущий каталог {os.getcwd()}')
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": delete_file,
    "cd": change_dir,
    "ls": file_list
}

try:
    trg_name=sys.argv[3]
except IndexError:
    trg_name=None

try:
    src_name = sys.argv[2]
except IndexError:
    src_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
