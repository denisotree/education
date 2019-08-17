import yaml
from socket import socket
from argparse import ArgumentParser

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
            print(f'Client send message {bytes_request.decode()}')

            client.send(bytes_request)
            client.close()
    except KeyboardInterrupt:
        print('Server turn off')
