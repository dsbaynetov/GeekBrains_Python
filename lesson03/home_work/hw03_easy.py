# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print ("\n### Задание 1.Easy")
def my_round(number, ndigits):
    int_number = int(number * (10 ** ndigits)+0.5)
    return (int_number / (10 ** ndigits))

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.1990967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print ("\n### Задание 2.Easy")
def lucky_ticket(ticket_number):
    tmp_list = list (str (ticket_number))
    sum1 = sum (list (int (itm) for itm in list (tmp_list[:3])))
    sum2 = sum (list (int (itm) for itm in list (tmp_list[3:])))
    return (sum1 == sum2)


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
