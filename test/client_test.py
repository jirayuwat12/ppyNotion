'''
test `Client` class
'''
import unittest
from ppyNotion.client import Client


class TestClient(unittest.TestCase):
    ''' test `Client` class '''

    def test_empty_init(self):
        ''' test empty init '''
        with self.assertRaises(ValueError):
            client_var = Client()

    def test_invalid_token_check_api(self):
        ''' init with invalid token but check api '''

        with self.assertRaises(ValueError):
            client_var = Client(token='secret....................')

        with self.assertRaises(ValueError):
            client_var = Client(token='wrong one')

    def test_invalid_token_not_check_api_(self):
        ''' init with invalid token but not check with API '''
        # absolutly wrong
        with self.assertRaises(ValueError):
            client_var = Client(token='wrong one', is_check_token=False)
        # right form but wrong api key
        client_var = Client(
            token='secret......................',
            is_check_token=False)

    def test_str_function(self):
        ''' init then test str function '''
        token = 'secret................'
        client_var = Client(token=token, is_check_token=False)
        self.assertEqual(str(client_var),f'client token = {token}')
