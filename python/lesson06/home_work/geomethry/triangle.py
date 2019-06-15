import math


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.a = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        self.b = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))
        self.c = math.sqrt(((x1 - x3) ** 2) + ((y1 - y3) ** 2))

    def per(self):
        return self.a + self.b + self.c

    def sq(self):
        p = self.per() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def hight(self):
        p = self.per() / 2
        ha = (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.a
        hb = (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.b
        hc = (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.c
        return ha, hb, hc


if __name__ == "__main__":
    trg1 = Triangle(1, 1, 2.5, 9, 5, 3)

    print(f'{trg1.sq():.3f}')

    print(f'{trg1.per():.3f}')

    heights = trg1.hight()

    print(f'{heights[0]:.3f}, {heights[1]:.3f}, {heights[2]:.3f}')
