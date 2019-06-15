# coding utf-8

print('Введите размеры трех отрезков:')
a = int(input('Первый отрезок: '))
b = int(input('Второй отрезок: '))
c = int(input('Третий отрезок: '))

if a + b < c or a + c < b or b + c < a:
    print('Такой треугольник не существует')
else:
    if a > b:
        if a > c:
            if b * b + c * c - a * a > 0:
                print('Остроугольный треугольник')
            elif b * b + c * c - a * a < 0:
                print('Тупоугольный треугольник')
            else:
                print('Прямоугольный треугольник')
        else:
            if b * b + a * a - c * c > 0:
                print('Остроугольный треугольник')
            elif b * b + a * a - c * c < 0:
                print('Тупоугольный треугольник')
            else:
                print('Прямоугольный треугольник')
    else:
        if b > c:
            if a * a + c * c - b * b > 0:
                print('Остроугольный треугольник')
            elif a * a + c * c - b * b < 0:
                print('Тупоугольный треугольник')
            else:
                print('Прямоугольный треугольник')
        else:
            if b * b + a * a - c * c > 0:
                print('Остроугольный треугольник')
            elif b * b + a * a - c * c < 0:
                print('Тупоугольный треугольник')
            else:
                print('Прямоугольный треугольник')



