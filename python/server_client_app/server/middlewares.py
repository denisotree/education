import zlib
from functools import wraps


def compression_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kargs):
        bytes_request = zlib.decompress(request)
        bytes_response = func(bytes_request, *args, **kargs)
        return zlib.compress(bytes_response)
    return wrapper
