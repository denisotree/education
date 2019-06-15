#!/usr/bin/python3
# coding utf-8

import random

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
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


class Card:
    def __init__(self):
        self.card = []

    def __repr__(self):
        result = ''
        for row in self.card:
            for column in row:
                result += str(f'{column:>3} ')
            result += '\n'
        return result

    def create_card(self):
        nums = random.sample(range(1, 91), 15)
        start = 0
        end = 5
        for i in range(3):
            row = []
            pos = sorted(random.sample(range(9), 5))
            sort_nums = sorted(nums[start:end])
            for j in range(0, 9):
                if j in pos:
                    pos_i = pos.index(j)
                    row.append(sort_nums[pos_i])
                else:
                    row.append('')
            self.card.append(row)
            start += 5
            end += 5

    def is_empty(self):
        return len([el for row in self.card for el in row if type(el) == int]) > 0

    def cross(self, number):
        for row in self.card:
            for i, el in enumerate(row):
                if number == el:
                    row[i] = 'x'
                    return True
        return False

    def has_number(self, number):
        for row in self.card:
            for i, el in enumerate(row):
                if number == el:
                    return True
        return False


class Lotto:
    def __init__(self, player_card, computer_card):
        self.player_card = player_card
        self.computer_card = computer_card
        self.play_bag = []

    def _show_play_screen(self, i, barrel):
        print("-" * 35)
        print("----------- Ваша карточка ----------")
        print(self.player_card)
        print("-" * 35)
        print("------- Карточка компьютера --------")
        print(self.computer_card)
        print("-" * 35)
        print(f"Новый бочонок: {barrel}. Осталось бочонков: {len(self.play_bag) - i - 1}")

    def _player_step(self, barrel):
        while True:
            answer = input("Зачеркнуть цифру? (y/n)? Или нажмите q для выхода: ")
            if answer == 'q':
                exit()
            elif answer == 'y':
                if not self.player_card.cross(barrel):
                    print("Такой цифры в карточке нет. Вы проиграли")
                    exit()
                break
            elif answer == 'n':
                if self.player_card.cross(barrel):
                    print("Такая цифра в карточке есть. Вы проиграли")
                    exit()
                break

    def _computer_step(self, barrel):
        if self.computer_card.has_number(barrel):
            print(f"Компьютер зачеркнул цифру {barrel}")
            self.computer_card.cross(barrel)
        else:
            print(f"В карточке компьютера нет цифры {barrel}")

    def _check_circs(self):
        if not self.player_card.is_empty() and not self.computer_card.is_empty():
            print("Ничья!")
            return True
        elif not self.player_card.is_empty():
            print("Вы выиграли!")
            return True
        elif not self.computer_card.is_empty():
            print("Вы выиграли!")
            return True
        return False

    def start_game(self):
        self.play_bag = random.sample(range(1, 91), 90)
        print("Добро пожаловать в игру «Лото»")
        for i, barrel in enumerate(self.play_bag):
            self._show_play_screen(i, barrel)
            self._player_step(barrel)
            self._computer_step(barrel)
            if self._check_circs():
                return


player_card = Card()
player_card.create_card()
computer_card = Card()
computer_card.create_card()

lotto = Lotto(player_card, computer_card)
lotto.start_game()
