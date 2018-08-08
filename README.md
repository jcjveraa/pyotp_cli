[![Build Status](https://travis-ci.org/jcjveraa/pyotp_cli.svg?branch=master)](https://travis-ci.org/jcjveraa/pyotp_cli)
[![Code coverage](https://codecov.io/gh/jcjveraa/pyotp_cli/branch/master/graph/badge.svg)](https://codecov.io/gh/jcjveraa/pyotp_cli/)
# pyotp_cli
Provides a command line interface for [pyotp](https://github.com/pyotp/pyotp) to interact more easily with other programs.

## usage
```
python -m pyotp_cli [-h] [-u user_name issuer_name] [-s secret] [-v otp secret validity_window] [-g]

optional arguments:
  -h, --help            show this help message and exit
  -u user_name issuer_name, --generate_provisioning_uri user_name issuer_name
                        Generates and returns a provisioning uri for user_name
                        and issuer_name.
  -s secret, --secret secret
                        Sets the secret. Optional with -u.
  -v otp secret validity_window, --verify otp secret validity_window
                        Validates if the TOTP is correct. Requires a to-be-
                        checked 6 digit OTP, a base32 encoded 16bit secret and
                        a validity_window which dictates the number of
                        previous/future values that will be acceptad as true.
  -g, --generate_16b32_secret
                        Generates and returns a 16 character base32 secret.`
```
