import unittest, os, base64
from pyotp_cli import pyotp_wrapper #noqa

try:
    from urllib.parse import urlparse, parse_qsl
except ImportError:
    from urlparse import urlparse, parse_qsl

class TestPyotpCLI(unittest.TestCase):

    def test_random_base32(self):
        random_string = pyotp_wrapper.random_base32()
        self.assertEqual(len(random_string), 16)
        chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
        for c in list(random_string):
            self.assertIn(c, chars)


    def test_generate_provisioning_uri(self):
        url = urlparse(
            pyotp_wrapper.generate_provisioning_uri('FooCorp!','mark@percival', 'wrn3pqx5uqxqvnqr' ))
        self.assertEqual(url.scheme, 'otpauth')
        self.assertEqual(url.netloc, 'totp')
        self.assertEqual(url.path, '/FooCorp%21:mark%40percival')
        self.assertEqual(dict(parse_qsl(url.query)),
                        {'secret': 'wrn3pqx5uqxqvnqr',
                        'issuer': 'FooCorp!'})

if __name__ == '__main__':
    unittest.main()