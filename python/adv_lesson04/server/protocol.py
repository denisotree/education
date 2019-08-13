import datetime


def validate_request(request):
    return True if 'action' in request and 'timestamp' in request else False


def make_response(code, data=None):
    return {
        'data': data,
        'code': code,
        'timestamp': datetime.datetime.now().timestamp()
    }