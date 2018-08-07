import unittest, os
from pyotp_cli import pyotp_wrapper #noqa

class TestPyotpCLI(unittest.TestCase):

    def test_main(self):
        result = pyotp_wrapper.random_base32()
        self.assertEqual(result, 0)
        # now check that the script's output is what you expect


if __name__ == '__main__':
    unittest.main()