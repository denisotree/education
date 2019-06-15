# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

# Задача оказалась довольно сложной, я нагуглил решение через очередь с
# приоритетами (http://practice.keyfire.ru/blog/kak-zakodirovat-stroku-s-pomoshyu-algoritma-haffmana/)и разобрался
# в нем дебагером

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(string):
    h = []
    for el, often in Counter(string).items():
        h.append((often, len(h), Leaf(el)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        often1, _count1, left = heapq.heappop(h)
        often2, _count2, right = heapq.heappop(h)

        heapq.heappush(h, (often1 + often2, count, Node(left, right)))

        count += 1
    code = {}
    if h:
        [(_often, _count, root)] = h
        root.walk(code, "")
    return code


string = input('Введите текстовую строку: ')
code = huffman_encode(string)
encoded = "".join(code[ch] for ch in string)

for ch in sorted(code):
    print(f"{ch}:\t{code[ch]}")
print(f'Строка «{encoded}» закодирована как:\n{encoded}')



