# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print ("\n### Задание 1.Normal")

def fibodigit(n):
    """
    Функция вычисления числа n ряда Фибоначи
    :param n: номер числа в ряду
    :return: число n в ряду Фибоначи
    """
    if n in (1, 2):
        return 1
    return fibodigit (n - 1) + fibodigit (n - 2)


def fibonacci(n, m):
    result = list (fibodigit (i) for i in range (1, m + 1) if i >= n)
    return result

print( fibonacci(1,10) )
print( fibonacci(4,10) )
print( fibonacci(4,8) )

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print ("\n### Задание 2.Normal")
def sort_to_max(origin_list):
    flag = True
    while flag:
        flag = False
        for i in range (len (origin_list) - 1):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
                flag = True
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

print ("\n### Задание 3.Normal")
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def my_filter(func, *args):
    tempo = list(*args)
    result = list( itm for itm in tempo if func(itm))
    return result


print(list(filter(lambda x: x%2, [10, 111, 102, 213, 314, 515])))
print(my_filter(lambda x: x%2, [10, 111, 102, 213, 314, 515]))

print ("\n### Задание 4.Normal")
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

def side_len(point1, point2):
    result = math.sqrt (abs(point1[0] - point2[0]) ** 2 + abs(point1[1] - point2[1]) ** 2)
    return result

def is_parall(a, b, c, d):
    #Проверка равенства сторон
    ab = side_len(a, b)
    bc = side_len(b, c)
    cd = side_len(c, d)
    ad = side_len(d, a)

    return (ab == cd) and (bc == ad)

a1, a2, a3, a4 = (2,2), (4,5), (10,5), (8,2)

print(is_parall(a1, a2, a3, a4))
