# coding utf-8

year = int(input('Введите год: '))

if year % 400 == 0:
    print(f'Год {year} високосный')
elif year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print(f'Год {year} не високосный')
elif year % 4 == 0:
    print(f'Год {year} високосный')
