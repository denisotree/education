# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def char_sum(n):
    sm = 0
    for i in str(n):
        sm += int(i)
    return sm


def max_value(array):
    mv = 0
    for arg in array:
        if arg > mv:
            mv = arg
    mi = array.index(mv)
    return mv, mi


numbers = [int(input('Введите натуральное число: ')) for i in range(5)]

sum_array = [char_sum(num) for num in numbers]

max_val, max_index = max_value(sum_array)

print(f'Самое большое число из введенных — {numbers[max_index]} с суммой цифр {max_val}')
