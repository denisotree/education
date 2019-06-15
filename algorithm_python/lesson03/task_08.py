# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

matrix = []
summa = 0

for i in range(4):
    matrix.append([])
    for j in range(5):
        if j < 4:
            matrix[i].append(int(input(f'Введите {j + 1} элемент {i + 1} строки: ')))
        else:
            for k in matrix[i]:
                summa += k
            matrix[i].append(summa)
            summa = 0

print('Итоговая матрица')

for line in matrix:
    print(line)
