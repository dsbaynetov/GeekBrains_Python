# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os, sys
from file_lib import create_folder, delete_file, copy_file, file_list


def create_dirs():
    for i in range(1, 10):
        # dir_name=os.getcwd()
        dir_name = "dir_{}".format(i)
        create_folder(dir_name)

def remove_dirs():
    for i in range(1, 10):
        # dir_name=os.getcwd()
        dir_name = "dir_{}".format(i)
        delete_file(dir_name)

if __name__ == '__main__':
    #создать подкаталоги dir_[1-9] в текущей папке
    print('Создать каталоги dir_[1-9] в "{}"'.format(os.getcwd()))
    create_dirs()
    print(os.listdir(os.getcwd()))

    print('Удалить каталоги dir_[1-9]')
    remove_dirs()
    print(os.listdir(os.getcwd()))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# получить список файлов и/или папок
if __name__ == '__main__':
    print('\nЗадача-2.Easy')
    print('Вывод списка файлов и каталогов')
    file_list(os.getcwd())
    print('Вывод только каталогов')
    file_list(os.getcwd(), True)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
if __name__ == '__main__':
    print('\nЗадача-3.Easy')
    file_src = sys.argv[0]
    file_dest = os.path.join(os.getcwd(), 'copy.py')
    copy_file(file_src, file_dest)
    print('Copy file name: ', file_dest)
