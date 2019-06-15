# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


def is_even(c):
    if int(c) % 2 == 0:
        return True
    else:
        return False


even = 0
not_even = 0
num = input('Введите натуральное число: ')

for c in num:
    if is_even(c):
        even += 1
    else:
        not_even += 1

print(f'В введенном числе {num}, {even} четных цифр и {not_even} нечетных')
