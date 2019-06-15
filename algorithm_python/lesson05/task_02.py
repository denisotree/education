# coding: utf-8

from collections import deque

# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# # элементы которого это цифры числа.
# #
# # Например, пользователь ввёл A2 и C4F.
# # Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# # Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# # Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

hex_num = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}


def list_to_str(lst):
    return ''.join(lst)


def hex_to_dec(hex_list):
    changed_list = deque()
    for el in hex_list:
        try:
            changed_list.append(int(el))
        except ValueError:
            if el in hex_num:
                changed_list.append(hex_num.get(el))
            else:
                print('Вы ввели неверное число')
                exit()
    return changed_list


def dec_to_hex(dec_list):
    changed_list = deque()
    for el in dec_list:
            if el > 9:
                char = {num: char for char, num in hex_num.items()}.get(el)
                changed_list.append(char)
            else:
                changed_list.append(str(el))
    return changed_list


def hex_sum(a, b):
    a = deque(a)
    b = deque(b)
    short = b if len(a) >= len(b) else a
    len_dif = abs(len(a) - len(b))
    for step in range(len_dif):
        short.appendleft(0)
    c = deque(map(sum, zip(a, b)))
    c.reverse()
    r = 0
    for i, num in enumerate(c):
        c[i] += r
        if num > 15:
            c[i] -= 16
            r = 1
        else:
            r = 0
    if r == 1:
        c.append(r)
    c.reverse()
    return c


# def hex_mult(a, b):
#     a = deque(a)
#     b = deque(b)
#     print(a, b, sep='\n')
#     prom = deque()
#     for i, el in enumerate(b):
#         line = []
#         for j in a:
#             line.append(el * j)
#         for _ in range(i):
#             line.append(0)
#         prom.append(line)
#     print(prom)


first_operand = list(input('Введите первый шестнадцатиричный операнд: ').upper())
second_operand = list(input('Введите второй шестнадцатиричный операнд: ').upper())

# first_operand = 'af2'.upper()
# second_operand = 'f3'.upper()

first_operand_hex = hex_to_dec(first_operand)
second_operand_hex = hex_to_dec(second_operand)

pre_result_sum = hex_sum(first_operand_hex, second_operand_hex)

# pre_result_mult = hex_mult(first_operand_hex, second_operand_hex)

result_sum = dec_to_hex(pre_result_sum)

first_operand_str = list_to_str(first_operand)
second_operand_str = list_to_str(second_operand)

result_sum_str = list_to_str(result_sum)

print(f'Результат сложения чисел {first_operand_str} и {second_operand_str} — {result_sum_str}')

