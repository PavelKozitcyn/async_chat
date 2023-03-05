import sys
import json
import socket
import time
from utils import *
from log.client_log_config import *


def create_presence(account_name='Paul'):
    out = {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'account_name': account_name
        }
    }
    return out


@MyLogger()
def process_ans(message):
    if 'response' in message:
        if message['response'] == 200:
            log.info('response OK')
            return '200 : OK'
        log.critical(f'400 : {message["error"]}')
        return f'400 : {message["error"]}'
    raise ValueError

@MyLogger()
def c_adress_cheker():
    try:
        server_adress = sys.argv[1]
    except IndexError:
        server_adress = '127.0.0.1'
        return server_adress
    except ValueError:
        log.critical('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

@MyLogger()
def c_port_cheker():
    try:
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_port = 7777
        return server_port
    except ValueError:
        log.critical('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)


def main():
    server_adress = c_adress_cheker()
    server_port = c_port_cheker()

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_adress, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        log.critical('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
