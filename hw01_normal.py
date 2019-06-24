__author__ = 'Байнетов Д.С.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

str_num=input("Введите целое число:")

max_num = 0
for i in range(len(str_num)):
    a = int(str_num[i])
    max_num = a if(a > max_num) else max_num

print(f"Максимальная цифра в числе {str_num} - {max_num}")


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
a=input("Введите переменную а: ")
b=input("Введите переменную b: ")

print(f"Исходные значения: a={a}, b={b}")
a,b = b,a
print(f"Меняем значения местами: a={a}, b={b}")

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
print("Задание-3. Вычисление корня квадратного уравнения вида: ax² + bx + c = 0")
a=int(input("Введите коэффициент а: "))
b=int(input("Введите коэффициент b: "))
c=int(input("Введите коэффициент c: "))

D = b**2 - 4*a*c
if (D < 0):
    print("Корней нет.")
elif (D == 0):
    x1 = (-1 * b + math.sqrt(D)) / 2 * a
    print(f"Есть один корень x={x1}")
elif (D > 0):
    x1 = (-1 * b + math.sqrt(D)) / 2 * a
    x2 = (-1 * b - math.sqrt(D)) / 2 * a
    print(f"Есть два корня.x1={x1}, x2={x2}")