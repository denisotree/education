from random import randint

# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше ее.


def custom_min(array):
    min_el = float('inf')
    for el in array:
        if el < min_el:
            min_el = el
    return min_el


def median(array):
    stack = []
    for i in range((len(array) // 2) + 1):
        # stack.append(array.pop(array.index(min(array)))) Через ф-цию min (не уверен, что ее можно юзать)
        stack.append(array.pop(array.index(custom_min(array))))  # Потому я добавил свою ф-цию min

    return stack.pop()


array = [randint(-50, 50) for i in range(11)]
print(f'Исходный массив\n{array}')
print(f'Медиана массива — {median(array)}')
