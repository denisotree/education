import logging
import json
from resolvers import resolve
from protocol import validate_request, make_response
from middlewares import compression_middleware


@compression_middleware
def handle_tcp_request(bytes_request):

    request = json.loads(
        bytes_request.decode()
    )

    if validate_request(request):
        action = request.get('action')
        controller = resolve(action)
        if controller:
            try:
                response = controller(request)
                logging.debug(f'Client send request {request}')
            except Exception as err:
                response = make_response(request, 500)
                logging.critical(f'Exception — {err}')
        else:
            logging.critical('Invalid action')
            response = make_response(request, 404)
    else:
        logging.critical('Invalid request')
        response = make_response(request, 404)

    string_response = json.dumps(response)
    return string_response.encode()
