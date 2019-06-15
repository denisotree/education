from hashlib import sha1
from hashlib import sha256

# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N.
# Например, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()


def substrings_count(st):
    len_str = len(st)
    suf_arr = set()
    f = 0
    for i in range(len_str):
        for j in range(i + 1, len_str + 1):
            f += 1
            hash_suf = sha1(st[i:j].encode())
            suf_arr.add(hash_suf.hexdigest())

    return len(suf_arr)


# string = 'papa'
# suffix_count = substrings_count(string)
#
# print(f'В строке {string} {suffix_count} уникальных подстрок')

print(sha256(b'Mike Andrew').hexdigest())
