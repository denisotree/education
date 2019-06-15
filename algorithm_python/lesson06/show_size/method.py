import sys


def show_size(x):
    type_ = type(x)
    size = sys.getsizeof(x)
    obj = x
    return type_, size, obj
