a = int(input('Введите целое трехзначное число: '))
c1 = int(a / 100)
c2 = int((a % 100) / 10)
c3 = int(a % 10)

_sum = c1 + c2 + c3
_prod = c1 * c2 * c3

print(f'Сумма цифр введенного числа {_sum}, произведение {_prod}')
