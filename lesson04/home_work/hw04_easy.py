# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print ("\n# Задание-1. Easy")
list1 = [1, 2, 4, 0]
result = [(item ** 2) for item in list1 ]
print(f"Исходный список {list1}")
print(f"Результирующий список {result}")

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print ("\n# Задание-2. Easy")
fruit1 = ["яблоко", "груша", "слива", "вишня", "банан", "абрикос"]
fruit2 = ["манго", "слива", "банан", "авокадо"]

result = [fruit for fruit in fruit1 if fruit in fruit2]
print(f"Список-1 {fruit1}")
print(f"Список-2 {fruit2}")
print(f"Результирующий список {result}")


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
print ("\n# Задание-3. Easy")
list1 = [random.randint(-100, 100) for item in range(0, 30)]
#list1 = [item for item in range(0, 20)]
list2 = [item for item in list1 if ((item %3 ==0) and (item > 0) and not (item % 4 == 0))]
print(f"Исходный список чисел: {list1}")
print(f"Результирующий список: {list2}")