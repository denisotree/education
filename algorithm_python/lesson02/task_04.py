# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

num = input('Введите длину ряда: ')
sum_numbers = 0
arr = []
d = 1
i = 0
while i < int(num):
    sum_numbers += d
    arr.append(d)
    d /= -2
    i += 1
print(f'Сумма ряда чисел {arr} — {sum_numbers} ')
