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
    sock = socket()
    sock.connect((config.get('address'), config.get('port')))

    print('Client was connected')

    data = input('Enter your message: ')
    sock.send(data.encode())
    print('Client send data')
    bytes_response = sock.recv(2048)
    print(bytes_response.decode())

    sock.close()
