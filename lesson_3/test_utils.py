import unittest
import subprocess
from client import create_presence
from utils import get_message, send_message
from server import main
import time
import socket


class TestUtils(unittest.TestCase):

    def test_get_message(self):
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect(('127.0.0.1', 7777))
        message_to_server = create_presence()
        send_message(transport, message_to_server)
        self.assertEqual(get_message(transport), {'response': 200})

    def test_send_message(self):
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect(('127.0.0.1', 7777))
        message_to_server = create_presence()
        self.assertEqual(send_message(transport, message_to_server), 1)


if __name__ == '__main__':
    unittest.main()
