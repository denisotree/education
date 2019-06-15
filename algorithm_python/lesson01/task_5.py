# coding utf-8

print('Введите две буквы:')
a = input('Первая буква: ')
b = input('Вторая буква: ')

a_asii = ord(a)
b_asii = ord(b)


if 97 <= a_asii <= 122 and 97 <= b_asii <= 122:
    a_pos = a_asii - 97
    b_pos = b_asii - 97
    dif = abs(a_pos - b_pos)
    print(f'Введенные буквы из латинского алфавита:\n'
          f'Буква {a} стоит на позиции {a_pos}\n'
          f'Буква {b} стоит на позиции {b_pos}\n'
          f'Между буквами {a} и {b} разница в {dif} символов')
elif 1072 <= a_asii <= 1103 and 1072 <= b_asii <= 1103:
    a_pos = a_asii - 1072
    b_pos = b_asii - 1072
    dif = abs(a_pos - b_pos)
    print(f'Введенные буквы из русского алфавита:\n'
          f'Буква {a} стоит на позиции {a_pos}\n'
          f'Буква {b} стоит на позиции {b_pos}\n'
          f'Между буквами {a} и {b} разница в {dif} символов')
else:
    print('Вы ввели неверные значения')
