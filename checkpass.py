#!/usr/bin/env python

import sys
import hashlib
import requests

if len(sys.argv) != 2:
    print("""Usage: ./checkpass.py <PASSWORD>
            -h for help menu""")
    exit(1)

def check(password):
    sha1sum = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1sum[:5]
    suffix = sha1sum[5:]

    try:
        r = requests.get("https://api.pwnedpasswords.com/range/{0}".format(prefix))
    except Exception as e:
        print("\nConnection error! {}".format(e))
        sys.exit(1)

    response = r.text.split('\r\n')

    for line in response:
        if suffix in line:
            num = line.split(':')[1]
            break
        else:
            num = 0

    return sha1sum, num

def main(password):
    sha1sum, num = check(password)
    
    if num:
        print("\n  Oops, the password '{}' has seen {} times before!\n".format(password, num))
    else:
        print("\n  Good news!!!\n")
    
    sys.exit()

if __name__ == '__main__':
    main(sys.argv[1])
