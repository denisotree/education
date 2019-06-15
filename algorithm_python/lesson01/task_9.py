# coding utf-8

print('Введите три числа:')
a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))

if b < a < c or c < a < b:
    print(f'Среднее число {a}')
elif a < b < c or c < b < a:
    print(f'Среднее число {b}')
elif a < c < b or b < c < a:
    print(f'Среднее число {c}')



