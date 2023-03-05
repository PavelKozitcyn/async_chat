import sys
import json
from socket import *
import time
from utils import *
from log.client_log_config import *

ADDRESS = ('localhost', 10000)


def echo_client():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            data = sock.recv(1024).decode('utf-8')
            if data:
                print('Ответ: ', data)


if __name__ == '__main__':
    echo_client()
