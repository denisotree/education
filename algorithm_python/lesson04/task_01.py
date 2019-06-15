# Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках
# домашнего задания первых трех уроков.

import random
import cProfile

# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.


def get_sum_matrix(n, m):
    matrix = []
    summa = 0

    for i in range(n):
        matrix.append([])
        for j in range(m):
            if j < 4:
                matrix[i].append(random.randint(0, 9))
            else:
                for k in matrix[i]:
                    summa += k
                matrix[i].append(summa)
                summa = 0
    return matrix

# "task_01.get_sum_matrix(4, 5)" 100 loops, best of 5: 31.3 usec per loop
# "task_01.get_sum_matrix(40, 50)" 100 loops, best of 5: 3.17 msec per loop
# "task_01.get_sum_matrix(80, 100)" 100 loops, best of 5: 23.6 msec per loop
# "task_01.get_sum_matrix(160, 200)" 100 loops, best of 5: 190 msec per loop

# cProfile.run('get_sum_matrix(4, 5)') 1    0.000    0.000    0.000    0.000 task_01.py:12(get_sum_matrix)
# cProfile.run('get_sum_matrix(40, 50)') 1    0.003    0.003    0.004    0.004 task_01.py:12(get_sum_matrix)
# cProfile.run('get_sum_matrix(80, 100)') 1    0.023    0.023    0.024    0.024 task_01.py:12(get_sum_matrix)
# cProfile.run('get_sum_matrix(160, 200)') 1    0.187    0.187    0.193    0.193 task_01.py:12(get_sum_matrix)


def get_sum_matrix_changed(n, m):
    matrix = []
    for i in range(n):
        summ = 0
        row = []
        for j in range(m-1):
            number = random.randint(0, 9)
            summ += number
            row.append(number)
        row.append(summ)
        matrix.append(row)
    return matrix


# "task_01.get_sum_matrix_changed(4, 5)" 100 loops, best of 5: 30.7 usec per loop
# "task_01.get_sum_matrix_changed(40, 50)" 100 loops, best of 5: 3.46 msec per loop
# "task_01.get_sum_matrix_changed(80, 100)" 100 loops, best of 5: 13.8 msec per loop
# "task_01.get_sum_matrix_changed(160, 200)" 100 loops, best of 5: 55.5 msec per loop

# cProfile.run('get_sum_matrix_changed(4, 5)') 1   0.000   0.000   0.000   0.000 task_01.py:39(get_sum_matrix_changed)
# cProfile.run('get_sum_matrix_changed(40, 50)') 1  0.001  0.001  0.006  0.006 task_01.py:39(get_sum_matrix_changed)
# cProfile.run('get_sum_matrix_changed(80, 100)') 1  0.004  0.004  0.023  0.023 task_01.py:39(get_sum_matrix_changed)
# cProfile.run('get_sum_matrix_changed(160, 200)') 1  0.016  0.016  0.090  0.090 task_01.py:39(get_sum_matrix_changed)


# Вывод

# Первый, мой, код менее эффективен — сумма столбцов высчитывается в цикле с тройной вложенностью. Во второй реализации
# из урока, вычисление ограничивается двумя циклами, что дает существенный прирост производительности
# на больших матрицах
