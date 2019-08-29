import yaml
from socket import socket
from argparse import ArgumentParser
import logging
from select import select

from handlers import handle_tcp_request

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
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=(
        logging.FileHandler('server.log'),
        logging.StreamHandler()
    )
)


if __name__ == '__main__':

    connections = []
    requests = []

    try:
        sock = socket()
        sock.bind((config.get('address'), config.get('port')))
        sock.settimeout(0)
        sock.listen(5)

        logging.info('Server started on localhost with port 8000')

        while True:
            try:
                client, address = sock.accept()
                client_host, client_port = address
                logging.info(f'Connect was detected {client_host}:{client_port}')
                connections.append(client)
            except:
                pass

            rlist, wlist, xlist = select(connections, connections, connections, 0)

            for read_client in rlist:
                bytes_request = read_client.recv(2048)
                requests.append(bytes_request)

            if requests:
                bytes_request = requests.pop()
                bytes_response = handle_tcp_request(bytes_request)

                for write_client in wlist:
                    write_client.send(bytes_response)

    except KeyboardInterrupt:
        logging.info('Server turn off')
