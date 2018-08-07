import argparse
from pyotp_cli.pyotp_wrapper import generate_provisioning_uri, random_base32, verify

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--generate_provisioning_uri", help="Generates and returns a provisioning uri for user_name and issuer_name.",
                    nargs=2, metavar=('user_name', 'issuer_name'))
parser.add_argument("-s", "--secret", help="Sets the secret. Optional with -u.",
                    nargs=1, metavar='secret')
parser.add_argument("-v", "--verify", help="Validates if the TOTP is correct. Requires a to-be-checked 6 digit OTP,\
                    a base32 encoded 16bit secret and a validity_window which dictates the number of previous/future values\
                    that will be acceptad as true.", nargs=3, metavar=('otp', 'secret' , 'validity_window'))
parser.add_argument("-g", "--generate_16b32_secret", help="Generates and returns a 16 character base32 secret.",
                    action="store_true")
        
args = parser.parse_args()

if args.generate_provisioning_uri:
    _a = args.generate_provisioning_uri
    secret = args.secret[0] if args.secret else None
    print(generate_provisioning_uri(_a[1],_a[0], secret=secret))

elif args.generate_16b32_secret:
    print(random_base32())

elif args.verify:
    _a = args.verify
    print(verify(_a[0], _a[1], int(_a[2])))
