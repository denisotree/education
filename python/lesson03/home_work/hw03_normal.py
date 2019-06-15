# coding utf-8

import math

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonatchi(n, m):
    #  Инициируем начало ряда
    f = [1, 1]
    i = 0
    #  Проверяем, не меньше ли начальное значение начала ряда
    if n < 1:
        return "Введено слишком маленькое значение"
    #  Строим ряд Фибоначчи
    while i < (m - 2):
        f.append(f[-1] + f[-2])
        i += 1
    #  Выводим значение с n-ного по m-ный элементы при помощи оператора среза
    return f[n - 1:m]


def fibonatchi_init():
    n = input('Введите начало ряда: ')
    m = input('Введите конец ряда: ')
    try:
        return fibonatchi(int(n), int(m))
    except ValueError:
        return 'Введены неверные значения'


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(sort_list):
    i = 1
    while i < len(sort_list):
        for el in range(len(sort_list) - i):
            #  Приводим элементы списка к их типу
            try:
                sort_list[el] = int(sort_list[el])
                sort_list[el + 1] = int(sort_list[el + 1])
            except ValueError:
                continue
            #  Меняем местами два соседних элемента ряда, если текущий больше следующего
            if sort_list[el] > sort_list[el + 1]:
                sort_list[el], sort_list[el + 1] = sort_list[el + 1], sort_list[el]
        i += 1
        #  Возвращаем отсортированный список
    return sort_list


def sort_to_max_init():
    lst = input('Введите элементы списка через запятую: ')
    lst = lst.split(', ')
    try:
        return sort_to_max(list(lst))
    except ValueError:
        return 'Введены неверные значения'


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


#  Задаем две функции для фильтрации

def more(x, n):
    if x > n:
        return 1
    else:
        return 0


def less(x, n):
    if x < n:
        return 1
    else:
        return 0


def filter_func(fn, lst):
    output = []
    #  Для каждого элемента списка проверяем на сооветствие условию функции
    for el in lst:
        if fn(el, 10):
            output.append(el)
    #  Выводим получившийся список
    return output


def filter_func_init():
    lst = input('Введите элементы списка через запятую: ')
    lst = lst.split(', ')
    try:
        lst = [int(item) for item in lst]
        return filter_func(less, lst)
    except ValueError:
        return 'Введены неверные значения'


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def par_gram(a1, a2, a3, a4):

    i = 0

    #  Проверяем разность веркоторов на признак паралеллограма

    if math.fabs(a1[0] - a2[0]) == math.fabs(a3[0] - a4[0]) and math.fabs(a1[1] - a2[1]) == math.fabs(a3[1] - a4[1]):
        i += 1

    if math.fabs(a1[0] - a3[0]) == math.fabs(a2[0] - a4[0]) and math.fabs(a1[1] - a3[1]) == math.fabs(a2[1] - a4[1]):
        i += 1

    if math.fabs(a1[0] - a4[0]) == math.fabs(a2[0] - a3[0]) and math.fabs(a1[1] - a4[1]) == math.fabs(a2[1] - a3[1]):
        i += 1

    #  Если проверка показывает признак паралеллаграмма, выводим True

    if i == 2:
        return True
    else:
        return False


def par_gram_init():
   a1 = input('Введите координаты первой точки: ').split(', ')
   a2 = input('Введите координаты второй точки: ').split(', ')
   a3 = input('Введите координаты третьей точки: ').split(', ')
   a4 = input('Введите координаты четвертой точки: ').split(', ')

   a1 = [int(item) for item in a1]
   a2 = [int(item) for item in a2]
   a3 = [int(item) for item in a3]
   a4 = [int(item) for item in a4]

   if par_gram(a1, a2, a3, a4):
       print('Это параллелограмм')
   else:
       print('Это не параллелограмм')


######################################################################################################
#  Интерфейс
######################################################################################################

while True:
    print(
         'Программа умеет:\n'
         '[1] Возвращать ряд Фибоначчи с n-элемента до m-элемента\n'
         '[2] Сортировать принимаемый список по возрастанию\n'
         '[3] Фильтровать список\n'
         '[4] Проверять точки на принадлежность к вершинам паралеллограма\n'
    )
    answer = input('Введите номер функции или нажмите [q] для выхода из программы: ')
    if answer == 'q':
        break
    elif not answer.isdigit():
        print('Вы ввели неверную команду')
    elif int(answer) == 1:
        print(fibonatchi_init())
    elif int(answer) == 2:
        print(sort_to_max_init())
    elif int(answer) == 3:
        print(filter_func_init())
    elif int(answer) == 4:
        par_gram_init()
    else:
        pass
