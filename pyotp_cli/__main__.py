import argparse
import pyotp
from pyotp_wrapper import generate_provisioning_uri, random_base32

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--generate_provisioning_uri", help="Generates and returns a provisioning uri for user_name and issuer_name.",
                    nargs=2, metavar=('user_name', 'issuer_name'))
parser.add_argument("-s", "--secret", help="Sets the secret. Optional with -u.",
                    nargs=1, metavar='secret')
parser.add_argument("-t", "--totp", help="Generates the TOTP belonging to the secret.", nargs=1, metavar='secret')
parser.add_argument("-g", "--generate_16b32_secret", help="Generates and returns a 16 character base32 secret.",
                    action="store_true")
        
args = parser.parse_args()

if args.generate_provisioning_uri:
    secret = args.secret[0] if args.secret else random_base32()
    print(pyotp.totp.TOTP(secret).provisioning_uri(args.generate_provisioning_uri[0], issuer_name=args.generate_provisioning_uri[1]))

elif args.generate_16b32_secret:
    print(random_base32())

elif args.totp:
    totp = pyotp.TOTP(args.totp[0])
    print(totp.now()) 
