import yaml
import json
import zlib
import datetime
import hashlib
from socket import socket
from argparse import ArgumentParser

READ_MODE = 'read'
WRITE_MODE = 'write'

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

parser.add_argument(
    '-m', '--mode', type=str, required=False, default=READ_MODE,
    help='Sets client mode'
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


if __name__ == '__main__':
    try:
        sock = socket()
        sock.connect((config.get('address'), config.get('port')))

        print('Client was connected')

        while True:
            if args.mode == WRITE_MODE:

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

            else:
                compressed_response = sock.recv(2048)
                bytes_response = zlib.decompress(compressed_response)
                print(bytes_response.decode())

    except KeyboardInterrupt:
        print('Client shutdown')
        sock.close()
