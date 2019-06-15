import cProfile

# Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,\
# 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199


def sieve_of_eratosthenes(n):
    ln = n
    res = []
    while len(res) < n:
        sieve = [i for i in range(ln)]
        sieve[1] = 0
        for i in range(2, ln):
            if sieve[i] != 0:
                j = i + i
                while j < ln:
                    sieve[j] = 0
                    j += i
        res = [i for i in sieve if i != 0]
        ln *= 2
    return res[n-1]

# "task_02.sieve_of_eratosthenes(10)" 100 loops, best of 5: 19.9 usec per loop
# "task_02.sieve_of_eratosthenes(100)" 100 loops, best of 5: 1.4 msec per loop
# "task_02.sieve_of_eratosthenes(1000)" 100 loops, best of 5: 46.6 msec per loop
# "task_02.sieve_of_eratosthenes(10000)" 100 loops, best of 5: 1.06 sec per loop


# cProfile.run('sieve_of_eratosthenes(10)') 1    0.000    0.000    0.000   0.000 task_02.py:10(sieve_of_eratosthenes)
# cProfile.run('sieve_of_eratosthenes(100)') 1    0.001    0.001    0.001   0.001 task_02.py:10(sieve_of_eratosthenes)
# cProfile.run('sieve_of_eratosthenes(1000)') 1    0.029    0.029    0.034   0.034 task_02.py:10(sieve_of_eratosthenes)
# cProfile.run('sieve_of_eratosthenes(10000)') 1    0.842    0.842    0.982   0.982 task_02.py:10(sieve_of_eratosthenes)


def get_prime(n):
    lst = [2]
    c = 3
    while len(lst) < n:
        if c % 2 == 0:
            c += 1
        d = 3
        while d * d <= c and c % d != 0:
            d += 2
        if d * d > c:
            lst.append(c)
            c += 1
        else:
            c += 1
    return lst[n-1]

# "import task_02" "task_02.get_prime(10)" 100 loops, best of 5: 7.38 usec per loop
# "import task_02" "task_02.get_prime(100)" 100 loops, best of 5: 233 usec per loop
# "import task_02" "task_02.get_prime(1000)" 100 loops, best of 5: 7.36 msec per loop
# "import task_02" "task_02.get_prime(10000)" 100 loops, best of 5: 234 msec per loop


# cProfile.run('get_prime(10)') 1    0.000    0.000    0.000    0.000 task_02.py:38(get_prime)
# cProfile.run('get_prime(100)') 1    0.000    0.000    0.000    0.000 task_02.py:38(get_prime)
# cProfile.run('get_prime(1000)') 1    0.008    0.008    0.009    0.009 task_02.py:38(get_prime)
# cProfile.run('get_prime(10000)') 1    0.241    0.241    0.247    0.247 task_02.py:38(get_prime)


# Так как я начал делать это ДЗ уже после начала следующего (вчерашнего) урока, я не мог уже использовать алгоритмы
# с разбора — для меня в решете Эратосфена большой проблемой была задача его размера, а вариант со словарем уже
# пролетел. Так что мое решето заведомо неэффективное, соответственно показывает результаты хуже обычного, хоть
# и оптимизированного перебора.

