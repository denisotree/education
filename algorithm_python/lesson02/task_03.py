# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# Простое решение

# num = input('Введите целое число: ')
# print(num[::-1])

# Решение через цикл

num = input('Введите целое число: ')
upend_num = []
for i in range(len(num)-1, -1, -1):
    upend_num.append(num[i])
upend_num = ''.join(upend_num)
print(f'Переворачиваем число {num} и получаем {upend_num}')
