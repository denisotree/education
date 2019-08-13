import yaml
import json
from socket import socket
from argparse import ArgumentParser

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


if __name__ == '__main__':
    try:
        sock = socket()
        sock.bind((config.get('address'), config.get('port')))
        sock.listen(5)

        print('Server started on localhost with port 8000')

        while True:
            client, address = sock.accept()
            client_host, client_port = address
            print(f'Connect was detected {client_host}:{client_port}')

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
                        print(f'Client send request {request}')
                    except Exception as err:
                        response = make_response(500)
                        print(f'Exception — {err}')
                else:
                    print('Invalid action')
                    response = make_response(404)
            else:
                print('Invalid request')
                response = make_response(404)

            client.send(json.dumps(response).encode())
            client.close()
    except KeyboardInterrupt:
        print('Server turn off')
