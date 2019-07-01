# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

a1 = '5/6 + 4/7'

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


def read_to_list(path):
    result = []
    with open(path, 'r', encoding='UTF-8') as f:
        list = [line.strip() for line in f]
        for item in list:
            result.append([i for i in item.split(' ') if len(i) > 0])
        return result


def build_dict_list(table):
    '''
    Строим список словарей из заголовка и списка
    :param table:
    :return:
    '''
    header = table.pop(0)
    return [dict(zip(header, item)) for item in table]


def merege_table(hours, workers):
    '''
    объединить таблицу работников и отработанне ими часы
    :param hours:
    :param workers:
    :return:
    '''

    for item1 in workers:
        for item2 in hours:
            if (item1['Фамилия'] == item2['Фамилия'] and item1['Имя'] == item2['Имя']):
                item1.update(item2)
    return workers


def calculate(table_in):
    for item in table_in:
        zp_sum = int(item['Зарплата'])
        norma_hs = int(item['Норма_часов'])
        work_hs = int(item['Отработано'])
        sum_in_hs = int(zp_sum / norma_hs)
        # расчет
        if work_hs == norma_hs:
            item['Результат'] = '%s' % (zp_sum)
        elif work_hs > norma_hs:
            item['Результат'] = '%s' % (zp_sum + (work_hs - norma_hs) * sum_in_hs * 2)
        else:
            item['Результат'] = '%s' % (sum_in_hs * work_hs)

    return table_in


# отработано часов
hours_list = read_to_list('data/hours_of')
hours = build_dict_list(hours_list)

# читаем таблицу сотрудников
workers_list = read_to_list('data/workers')
workers = build_dict_list(workers_list)

merege_table(hours, workers)
calculate(workers)

# сохранить в файл
with open('data/result.txt', 'w', encoding='UTF-8') as f:
    header = '{:<20}{:<20}{:<10}\n'.format('Имя', 'Фамилия', 'Результат')
    f.write(header)
    for item in workers:
        line = '{:<20}{:<20}{:<10}\n'.format(item['Имя'], item['Фамилия'], item['Результат'])
        f.write(line)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
import os


def save_fruit(item):
    # сформировать имя файла
    file_name = 'fruits_{}.txt'.format(item[0])
    path = os.path.join('sort_fruits', file_name)
    with open(path, 'a', encoding='UTF-8') as f:
        f.write('{}\n'.format(item))


'''
Читаем список фруктов
'''
path = 'data/fruits.txt'
with open(path, 'r', encoding='UTF-8') as f:
    fruits: list = [line.strip() for line in f if len(line.strip()) > 0]
    print(fruits)

if (not os.path.exists('sort_fruits')):
    os.mkdir('sort_fruits')

for item in fruits:
    save_fruit(item)
