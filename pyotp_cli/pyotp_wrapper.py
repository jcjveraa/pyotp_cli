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

def generate_provisioning_uri(issuer_name, user_name, secret=None):
    secret = secret or random_base32()
    print(pyotp.totp.TOTP(secret).provisioning_uri(user_name, issuer_name=issuer_name))

# elif args.generate_16b32_secret:
#     print(random_base32())

# elif args.totp:
#     totp = pyotp.TOTP(args.totp[0])
#     print(totp.now()) 
