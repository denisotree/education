import random
# Определить, какое число в массиве встречается чаще всего.

START_VAL = 0
END_VAL = 9

arr = [random.randint(START_VAL, END_VAL) for _ in range(100)]

arr_set = set(arr)
max_common = None
max_common_qt = 0

for i in arr_set:
    qt = arr.count(i)
    if qt > max_common_qt:
        max_common_qt = qt
        max_common = i

print(f'В массиве {arr} чаще всего встречается число {max_common} — {max_common_qt} раз')
