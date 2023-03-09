import unittest
from server import check_port, check_adress, process_client_message
import time


class TestServer(unittest.TestCase):

    def test_check_port(self):
        self.assertEqual(check_port(), 7777)

    def test_check_adress(self):
        self.assertEqual(check_adress(), '')

    def test_process_client_message(self):
        message = {
            'action': 'presence',
            'time': time.time(),
            'user': {
                'account_name': 'Guest'
            }
        }
        self.assertEqual(process_client_message(message), {'response': 200})

    def test_bad_process_client_message(self):
        message = {
            'action': 'sdf',

        }
        self.assertEqual(process_client_message(message), {'response': 400, 'error': 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
