import random

# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

START_VAL = 0
END_VAL = 150

arr = [random.randint(START_VAL, END_VAL) for _ in range(100)]

min_el = min_second_el = END_VAL

for el in arr:
    if el <= min_el:
        min_second_el = min_el
        min_el = el

print(f'В массиве {arr}:')
print(f'Два наименьших числа: {min_el} и {min_second_el}')
