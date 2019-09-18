import yaml
import json
import zlib
import datetime
import threading
import hashlib
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


def make_request(action, data, token=None):
    return {
        'action': action,
        'data': data,
        'timestamp': datetime.datetime.now().timestamp(),
        'token': token
    }


def read(sock, buffersize=2048):
    while True:
        compressed_response = sock.recv(buffersize)
        bytes_response = zlib.decompress(compressed_response)
        print(bytes_response.decode())


if __name__ == '__main__':
    try:
        sock = socket()
        sock.connect((config.get('address'), config.get('port')))

        print('Client was connected')

        read_thread = threading.Thread(target=read, args=(
            sock, 2048
        ))
        read_thread.start()

        while True:
            action = input('Enter action (echo | date): ')
            data = input('Enter your message: ')

            hash_obj = hashlib.sha256()
            hash_obj.update(
                str(datetime.datetime.now().timestamp()).encode()
            )

            request = make_request(action, data, hash_obj.hexdigest())
            str_request = json.dumps(request)
            bytes_request = zlib.compress(str_request.encode())

            sock.send(bytes_request)
            print('Client send data')

    except KeyboardInterrupt:
        print('Client shutdown')
        sock.close()
