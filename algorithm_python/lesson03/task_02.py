import random

# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 – если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

arr = [random.randint(1, 100) for _ in range(66)]

arr_inx = [i for i, el in enumerate(arr) if arr[i] % 2 == 0]

print(f'В массиве {arr}')
print(f'Четные числа стоят на позициях {arr_inx}')
