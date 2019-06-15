# Здесь я постарался реализовать задачу только классами, так как не уверен, что класс треугольника можно было писать так


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


class Segment:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def _length(self):
        p = self.a - self.b
        return (p.x * p.x + p.y * p.y) ** 0.5

    # @property
    # def slope(self):
    #     p = self.a - self.b
    #     return p.y / p.x


class Trapezium:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.s1 = Segment(a, b)
        self.s2 = Segment(b, c)
        self.s3 = Segment(c, d)
        self.s4 = Segment(d, a)

    def is_equfem(self):
        return (self.s2._length == self.s4._length) or (
                    self.s1._length == self.s3._length)

    def perimeter(self):
        return self.s1._length + self.s2._length + self.s3._length + self.s4._length

    def sq(self):
        s1l = self.s1._length
        s2l = self.s2._length
        s3l = self.s3._length
        s4l = self.s4._length
        return (s2l + s4l) / 2 * (s1l ** 2 - (s1l ** 2 - s3l ** 2 + (s4l - s2l) ** 2) / (2 * (s4l - s2l))) ** 0.5


if __name__ == '__main__':

    a = Point(2, 4)
    b = Point(0, 2)
    c = Point(0, 7)
    d = Point(2, 5)
    trapezium = Trapezium(a, b, c, d)
    print("Это равнобедренная трапеция") if trapezium.is_equfem() else print('Это не равнобедренная трапеция')
    print(f"Периметр трапеции = {trapezium.perimeter():.2f}")
    print(f"Площадь трапеции = {trapezium.sq():.2f}")