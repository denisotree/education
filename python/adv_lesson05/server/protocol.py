import datetime


def validate_request(request):
    return True if 'action' in request and 'timestamp' in request else False


def make_response(request, code, data=None):
    return {
        'action': request.get('action'),
        'data': data,
        'code': code,
        'timestamp': datetime.datetime.now().timestamp()
    }