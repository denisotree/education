import random

# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


def num_quantity(arr, num):
    q = 0
    for i in arr:
        if i == num:
            q += 1
    return q


length = int(input('Введите количество цифр в числовой последовательности: '))
number = int(input('Введите цифру, которую нужно посчитать: '))

range_ = [random.randint(1, 9) for i in range(length)]

print(f'Цифра {number} встречается в слчайной последовательности из {length} целых чисел'
      f' {num_quantity(range_, number)} раз')
