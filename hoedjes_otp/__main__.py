import argparse
import pyotp

# whole function Can be removed if pyotp accepts my pull request
def random_base32(length=16, random=None,
                  chars=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')):

    # Use secrets module if available (Python version >= 3.6) per PEP 506.
    try:
        import secrets
        random = secrets.SystemRandom()
    except ImportError:
        import random as _random
        random = _random.SystemRandom()
    return ''.join(
        random.choice(chars)
        for _ in range(length)
    )

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
