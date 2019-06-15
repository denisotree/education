import random

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

START_VAL = 1
END_VAL = 999

arr = [random.randint(START_VAL, END_VAL) for _ in range(10)]

min_idx = max_idx = max_el = 0
min_el = END_VAL

for i, el in enumerate(arr):
    if el > max_el:
        max_el = el
        max_idx = i
    elif el < min_el:
        min_el = el
        min_idx = i

print(f'В массиве {arr} максимальное значение {max_el}, минимальное {min_el}')
arr[min_idx], arr[max_idx] = arr[max_idx], arr[min_idx]
print(f'Меняем их местами, получается\n{arr}')

