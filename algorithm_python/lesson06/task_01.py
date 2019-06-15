from sys import version
from platform import machine
from show_size import show_size

year = 20

if year % 400 == 0:
    print(f'Год {year} високосный')
elif year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print(f'Год {year} не високосный')
elif year % 4 == 0:
    print(f'Год {year} високосный')


if __name__ == '__main__':
    type_, size_, object_ = show_size(year)
    print(f'В этой задаче одна переменная year, типа {type_}')
    print(f'Она хранит значение «{object_}» и занимает {size_} байт в памяти')
    print(f'Система: {machine()}, версия Python {version}')

# _________________________________________________________
#
# В этой задаче одна переменная year, типа <class 'int'>
# Она хранит значение «2098» и занимает 28 байт в памяти
# Система: x86_64, версия Python 3.7.1 (default, Nov  6 2018, 18:46:03)
# [Clang 10.0.0 (clang-1000.11.45.5)]
# _________________________________________________________

# Так как в этой задаче всего одна переменная, и та, хранящая только значение типа int, она будет очень долго
# занимать 28 байт.
