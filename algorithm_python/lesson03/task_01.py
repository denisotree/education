# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

diap = [i for i in range(2, 100)]

mult_diap = [len([j for j in diap if j % i == 0]) for i in range(2, 10)]

print(f'В диапазоне натуральных чисел от 2 до 99:')

for i, el in enumerate(mult_diap):
    print(f'Числу {i+2} кратно {mult_diap[i]} чител')

