# coding utf-8

import random

print('Выберите тип значения, которое нужно сгенерировать:\n'
      '[i] — целое число\n'
      '[f] - вещественное число\n'
      '[c] - символ от a до z')

asw = input('Ваш выбор: ')

if asw == 'i':
    print('Введите диапазон целых чисел')
    start = int(input('Введите начало диапазона: '))
    end = int(input('Введите конец диапазона: '))
    print(f'Случайное число: {int(random.random() * (end - start + 1)) + start}')

elif asw == 'f':
    print('Введите диапазон вещественных чисел')
    start = float(input('Введите начало диапазона: '))
    end = float(input('Введите конец диапазона: '))
    print(f'Случайное число: {(random.random() * (end - start) + start):.3f}')

elif asw == 'c':
    print('Введите диапазон букв от a до z')
    start = ord(input('Введите начало диапазона: '))
    end = ord(input('Введите конец диапазона: '))
    print(f'Случайное число: {chr(int(random.random() * (end - start + 1)) + start)}')

else:
    print('В ввели неверное значение')


