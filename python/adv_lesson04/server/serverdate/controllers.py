import datetime
from protocol import make_response


def date_controller(request):
    return make_response(200, datetime.datetime.now().timestamp())

