#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random

class CardLoto:
    def __init__(self, name = "Игрок"):
        self.name = name
        self.cross_amount = 0 #max 15

        # Формируем карточку 3х9 без цифр (заполненная нулями)
        self.card = [[0] * 9 for i in range(3)]

        #массив зачеркнутых ячеек
        self.cross_cell  = [[False] * 9 for i in range(3)]

        # сформировать последовательность цифр
        self.__numbers = [item for item in range(1, 100)]

        for i in range(0, 3):
            # сформировать список из 5-ти случайных ячеек в ряду
            indx = [i for i in range(0, 9)]
            indx_list = []

            # список из 5-ти случайных чисел
            line = []
            for _ in range(0, 5):
                # выбрать случайную ячейку в строке
                j = indx.pop(random.randint(0, len(indx) - 1))
                indx_list.append(j)

                # выбираем случайную цифру и удаляем ее из последовательности
                n = self.__numbers.pop(random.randint(0, len(self.__numbers) - 1))
                line.append(n)

            # сформировать карточку
            indx_list.sort()
            line.sort()

            for j in indx_list:
                self.card[i][j] = line.pop(0)



    def __str__(self):
        result = ''
        for i in range(0, 3):

            for j in range(0, 9):
                if (self.card[i][j] == 0):
                    result += '|   '
                else:
                    result += '| - ' if self.cross_cell[i][j] else '| {:2}'.format(self.card[i][j])
            result +='\n'
        return result

    def check_num(self, value):
        '''
        Проверка наличия цифры в карточке
        :param number: int
        :return true/false:
        '''
        result = False
        for i in range(0, len(self.card)):
            result = value in self.card[i]
            if (result):
                break
        return result

    def cross_out(self, value):
        result = False
        for i in range(0, len(self.card)):
            if (value in self.card[i]):
                indx =  self.card[i].index(value)
                self.cross_cell[i][indx] = True
                result  = True
                break
        return result


#раздать карточки
card1 = CardLoto("Игрок №1")
card2 = CardLoto("Компьютер")

card_list = []
card_list.append(card1)
card_list.append(card2)

#перемешать бочонки
numbers = [item for item in range(1, 100)]
command = ''
current_card = card_list[0]
next_value = True

while (command != 'q') and (len(numbers) > 0):
    #проверяем сколько закрыто чисел
    #TODO добавить проверку сколько закрыто чисел

    #Достаем бочонок
    if next_value:
        num = numbers.pop(random.randint(0, len(numbers) - 1))

    next_value = True
    print(''.ljust(20, "="))
    print(f'Новый бочонок:  {num} (осталось {len(numbers)})')
    print(''.ljust(20, "="))


    # выводим карточки игроков
    for card in card_list:
        print(f"\n=== Карточка игрока: {card.name}")
        print(card)

    # закрываем цифру в карточке компьютера, если она у него есть
    card2.cross_out(num)

    #запрос игроку
    command = input("Зачеркнуть цифру? (y/n)")
    if command.lower() == 'y':
        # Если нажали зачеркнуть, а цифры такой нет - проигрыш
        if not current_card.cross_out(num):
            command = 'q'
            print(f'Проиграл "{current_card.name}". Нет такой цифры в карточке')

    elif command.lower() == 'n':
        # Если игрок выбрал "продолжить":
        # Если цифра есть на карточке - игрок проигрывает и игра завершается.
        # Если цифры на карточке нет - игра продолжается.
        if current_card.check_num(num):
            command = 'q'
            print(f'Проиграл "{current_card.name}". Пропустил цифру. Нужно быть внимательнее')
    elif command.lower() == 'q':
        print("Игра завершена. Выход по желанию пользователя")
    else:
        next_value = False

