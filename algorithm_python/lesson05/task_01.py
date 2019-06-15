# coding: utf-8

from collections import namedtuple
from random import randint

# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


Firm = namedtuple('Firm', ['name', 'qprofit1', 'qprofit2', 'qprofit3', 'qprofit4', 'yprofit'])
Firm.__new__.__defaults__ = ('Firm', 0, 0, 0, 0, 0)

# firms = [
#     Firm(name='Apple', qprofit1=randint(10000000, 999999999), qprofit2=randint(10000000, 999999999), qprofit3=randint(10000000, 999999999), qprofit4=randint(10000000, 999999999)),
#     Firm(name='Samsung', qprofit1=randint(10000000, 999999999), qprofit2=randint(10000000, 999999999), qprofit3=randint(10000000, 999999999), qprofit4=randint(10000000, 999999999)),
#     Firm(name='Google', qprofit1=randint(10000000, 999999999), qprofit2=randint(10000000, 999999999), qprofit3=randint(10000000, 999999999), qprofit4=randint(10000000, 999999999)),
#     Firm(name='Amazon', qprofit1=randint(10000000, 999999999), qprofit2=randint(10000000, 999999999), qprofit3=randint(10000000, 999999999), qprofit4=randint(10000000, 999999999))
#     ]

firms = []
asw = 'y'

while asw != 'n' and asw != 'N':
    if asw == 'y' or asw == 'Y':
        name = input('Введите имя компании: ')
        qprofit1 = float(input('Введите прибыль за первый квартал: '))
        qprofit2 = float(input('Введите прибыль за второй квартал: '))
        qprofit3 = float(input('Введите прибыль за третий квартал: '))
        qprofit4 = float(input('Введите прибыль за четвертый квартал: '))

        firm = Firm(name, qprofit1, qprofit2, qprofit3, qprofit4)

        firms.append(firm)
    else:
        print('Введите y или n \n')

    asw = input('Вы хотите добавить еще компанию? (y/n) ')

for i, firm in enumerate(firms):
    firms[i] = firm._replace(yprofit=sum([firm.qprofit1, firm.qprofit2, firm.qprofit3, firm.qprofit4]))

midleprofit = sum([firm.yprofit for firm in firms]) / len(firms)

more = []
less = []

for firm in firms:
    if firm.yprofit > midleprofit:
        more.append((firm.name, firm.yprofit))
    else:
        less.append((firm.name, firm.yprofit))

print(f'\nСредняя годовая прибыль ${midleprofit}')
print('\nИз введенных компаний прибыль выше среднего у компаний: ')
[print(f'{el[0]} с прибылью ${el[1]}') for el in more]
print('\n')
print('Меньше среднего у компаний: ')
[print(f'{el[0]} с прибылью ${el[1]}') for el in less]
