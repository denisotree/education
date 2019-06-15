import random
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

START_VAL = -50
END_VAL = 50

arr = [random.randint(START_VAL, END_VAL) for _ in range(50)]

i = 0
idx = -1
for i, el in enumerate(arr):
    if el < 0 and idx == -1:
        idx = i
    elif arr[idx] < el < 0:
        idx = i

print(f'Максимальное отрицательное число в массиве {arr} — {arr[idx]}, стоящее на позиции {idx}')

