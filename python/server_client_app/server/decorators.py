import logging
from functools import wraps


logger = logging.getLogger('server.decorators')


def logged(log_format):
    def decorator(func):
        def wrapper(request):
            response = func(request)
            try:
                logger.debug(log_format % {'name': func.__name__, 'request': request, 'response': response})
            except Exception as err:
                print(err)
            return response
        return wrapper
    return decorator
