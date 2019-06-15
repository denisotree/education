# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n – любое натуральное число.

n = input('Введите любое натуральное число: ')
try:
    n = int(n)
    range_sum = 0

    for i in range(1, n + 1):
        range_sum += i

    expression = n * (n + 1) / 2

    if range_sum == expression:
        print(f'Равенство верно. Обе его части равны {range_sum}')
    else:
        print(f'Равенство не верно. Левая его часть равна {range_sum}, а правая {expression}')
except ValueError:
    print('Вы ввели неверное значение')
