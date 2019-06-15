from sys import version
from platform import machine
from show_size import show_size

num = input('Введите целое число: ')
append_num = []
for i in range(len(num)-1, -1, -1):
    append_num.append(num[i])
# upend_num = ''.join(upend_num)
# print(f'Переворачиваем число {num} и получаем {append_num}')


if __name__ == '__main__':
    sum_all = sum_iter = 0
    type_num, size_num, object_num = show_size(num)
    type_append_num, size_append_num, object_append_num = show_size(append_num)
    print(f'В этой задаче две переменные — num, типа {type_num} и append_num типа {type_append_num}')
    print(f'Переменная num хранит значение «{object_num}» и занимает {size_num} байт в памяти')
    print(f'Переменная append_num хранит значение «{object_append_num}» и занимает {size_append_num} байт в памяти.\n'
          f'Внутри лежат объекты: ')
    for item in append_num:
        type_item, size_item, object_item = show_size(item)
        print(f'Объект типа {type_item} со значением «{object_item}» занимает {size_item} байт в памяти')
        sum_iter += size_item
    sum_all = sum([size_num, size_append_num, sum_iter])

    print(f'Все переменные занимают в памяти {sum_all} байт')
    print(f'Система: {machine()}, версия Python {version}')


# В этой задаче две переменные — num, типа <class 'str'> и append_num типа <class 'list'>
# Переменная num хранит значение «828464» и занимает 55 байт в памяти
# Переменная append_num хранит значение «['4', '6', '4', '8', '2', '8']» и занимает 128 байт в памяти.
# Внутри лежат объекты:
# Объект типа <class 'str'> со значением «4» занимает 50 байт в памяти
# Объект типа <class 'str'> со значением «6» занимает 50 байт в памяти
# Объект типа <class 'str'> со значением «4» занимает 50 байт в памяти
# Объект типа <class 'str'> со значением «8» занимает 50 байт в памяти
# Объект типа <class 'str'> со значением «2» занимает 50 байт в памяти
# Объект типа <class 'str'> со значением «8» занимает 50 байт в памяти
# Все переменные занимают в памяти 483 байт
# Система: x86_64, версия Python 3.7.1 (default, Nov  6 2018, 18:46:03)
# [Clang 10.0.0 (clang-1000.11.45.5)]

# Данная задача намного затратнее по памяти за счет списка и строк внутри. Это показывает ее неэффективность
# в использовании памяти.
# Если переписать решение через деление на 10 получится существенная экономия.
# Откровенно не понял, как вытащить из цикла переменную i для оценки. Знаю только, что она добавит 28 байт

num = int(input('Введите целое число: '))
res = 0
while num > 0:
    res = res * 10 + num % 10
    num = num // 10

type_num, size_num, object_num = show_size(num)
type_res, size_res, object_res= show_size(res)
print(f'В этой задаче две переменные — num, типа {type_num} и res типа {type_res}')
print(f'Переменная num хранит значение «{object_num}» и занимает {size_num} байт в памяти')
print(f'Переменная res хранит значение «{object_res}» и занимает {size_res} байт в памяти.')
sum_all = size_num + size_res

print(f'Все переменные занимают в памяти {sum_all} байт')
print(f'Система: {machine()}, версия Python {version}')

# В этой задаче две переменные — num, типа <class 'int'> и res типа <class 'int'>
# Переменная num хранит значение «0» и занимает 24 байт в памяти
# Переменная res хранит значение «464828» и занимает 28 байт в памяти.
# Все переменные занимают в памяти 52 байт
# Система: x86_64, версия Python 3.7.1 (default, Nov  6 2018, 18:46:03)
# [Clang 10.0.0 (clang-1000.11.45.5)]

# Экономия памяти получается более чем в 10 раз
