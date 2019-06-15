import random

# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

START_VAL = 0
END_VAL = 150

arr = [random.randint(START_VAL, END_VAL) for _ in range(100)]

min_idx = max_idx = max_el = summa = 0
min_el = END_VAL

for i, el in enumerate(arr):
    if el > max_el:
        max_el = el
        max_idx = i
    elif el < min_el:
        min_el = el
        min_idx = i

if min_idx > max_idx:
    min_idx, max_idx = max_idx, min_idx

for i in range(min_idx + 1, max_idx):
    summa += arr[i]

print(f'В списке {arr}')
print(f'Минимальное значение: {min_el}')
print(f'Максимальное значение: {max_el}')
print(f'Сумма чисел между мнимальным и максимальным значениями: {summa}')