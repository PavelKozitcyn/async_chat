import json
from socket import *
import time
import sys
from utils import *
from log.server_log_config import *


@MyServerLogger()
def process_client_message(message):
    if 'action' in message and message['action'] == 'presence' and 'time' in message \
            and 'user' in message and message['user']['account_name'] == 'Paul':
        log.info('OK')
        return {'response': 200}
    log.critical('Bad request')
    return {
        'response': 400,
        'error': 'Bad Request'
    }


@MyServerLogger()
def check_port():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = 7777
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        log.critical('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        log.critical('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    return listen_port


@MyServerLogger()
def check_adress():
    try:
        if '-a' in sys.argv:
            listen_adress = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_adress = ''

    except IndexError:
        log.critical(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)
    return listen_adress


@MyServerLogger()
def handler_message(a):
    transport = a
    while True:
        client, client_adress = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
            return 1
        except (ValueError, json.JSONDecodeError):
            log.critical('Принято некорретное сообщение от клиента.')
            client.close()
            return 1


def main():
    listen_port = check_port()
    listen_adress = check_adress()

    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((listen_adress, listen_port))

    transport.listen(5)

    handler_message(transport)


if __name__ == '__main__':
    main()
