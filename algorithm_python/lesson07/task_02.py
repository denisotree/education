from random import uniform

# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.


def merge_sort(array):
    if len(array) > 1:  # Отсекаем общий случай
        sep = len(array) // 2  # Делим исходный массив на две части
        left_arr = array[:sep]
        right_arr = array[sep:]

        merge_sort(left_arr)  # Рекурсивно вызываем функцию, чтобы разрдобить массив
        merge_sort(right_arr)  # на отдельные цифры

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:  # Постепенно сливаем правую и левую часть в основной массив
                array[k] = left_arr[i]  # Первичная проверка — если левая часть больше, она становится на первое место
                i += 1
            else:
                array[k] = right_arr[j]  # Если нет, туда заходит вторая
                j += 1
            k += 1

        while i < len(left_arr):  # Тут мы проверяем — если левая часть еще не встала на первое место в массиве
            array[k] = left_arr[i]  # Устанавливаем ее на вторую позицию
            i += 1
            k += 1

        while j < len(right_arr):  # Аналогично поступаем с правой частью
            array[k] = right_arr[j]
            j += 1
            k += 1
        return array  # Возвращаем массив для новой итерации или для выхода


array = [uniform(0, 50) for i in range(10)]
print(f'Исходный массив\n{array}')
print(f'Отсортированный массив\n{merge_sort(array)}')
