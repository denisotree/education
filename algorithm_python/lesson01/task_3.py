print('Введите координаты точек прямой')
x1 = float(input('x1: '))
x2 = float(input('x2: '))
y1 = float(input('y1: '))
y2 = float(input('y2: '))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'Уравнение прямой, проходящей чере точки А({x1}, {x2}) и B({y1}, {y2}): y = {k:.3f} * x + {b:.3f}')
