a = 5
b = 6

_and = a & b
_or = a | b

_ml = a << 2
_mr = a >> 2

print(f'Десятичный результат логического умножения {_and}')
print(f'Двоичный результат логического умножения {bin(_and)}')
print(f'Десятичный результат логического сложения {_or}')
print(f'Двоичный результат логического сложения {bin(_or)}')
# Если я правильно помню, при побитовом сдвиге влево в бинарном представлении числа происходит прибавление нулевых
# битов справа, а при побитовом сдвиге вправо "съедаются" крайние справа знаки
print(f'Десятичный результат побитового сдвига влево {_ml}')
print(f'Двоичный результат побитового сдвига влево {bin(_ml)}')
print(f'Десятичный результат побитового сдвига вправо {_mr}')
print(f'Двоичный результат побитового сдвига вправо {bin(_mr)}')