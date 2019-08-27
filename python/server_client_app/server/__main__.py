import yaml
import json
from socket import socket
from argparse import ArgumentParser
import logging

from resolvers import resolve
from protocol import validate_request, make_response

config = {
    'address': '127.0.0.1',
    'port': 7777,
    'buffer_length': 2048
}

parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str, required=False,
    help="Use config file"
)

parser.add_argument(
    '-a', '--address', type=str, required=False,
    help='Sets host address'
)

parser.add_argument(
    '-p', '--port', type=str, required=False,
    help='Sets host port'
)

args = parser.parse_args()

if args.config:
    with open(args.config) as f:
        config_file = yaml.safe_load(f)
        config.update(config_file or {})

if args.address:
    config['address'] = args.address

if args.port:
    config['port'] = args.port

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s — %(message)s',
    handlers=(
        logging.FileHandler('server.log'),
        logging.StreamHandler()
    )
)


if __name__ == '__main__':
    try:
        sock = socket()
        sock.bind((config.get('address'), config.get('port')))
        sock.listen(5)

        logging.info('Server started on localhost with port 8000')

        while True:
            client, address = sock.accept()
            client_host, client_port = address
            logging.info(f'Connect was detected {client_host}:{client_port}')

            bytes_request = client.recv(2048)

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

            client.send(json.dumps(response).encode())
            client.close()
    except KeyboardInterrupt:
        logging.info('Server turn off')
