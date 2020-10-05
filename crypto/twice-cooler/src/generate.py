#!/usr/bin/env python3

import base64
import sys


ROUNDS = 24
DEBUG = True

text = b'BCTF{base32_is_c00ler_than_base64_s0meh0w}'


def debug(s, end='\n'):
    if DEBUG:
        print(s, end=end)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        DEBUG = False
        ROUNDS = int(sys.argv[1])

    for i in range(1, ROUNDS + 1):
        text = base64.b32encode(text)

        debug(i, end='\t')
        if text[-1] == ord('='):
            # extra peculiarity: we want to hide "=" at the end of output
            # to not give extra hint about base32/base64 encoding.
            debug('ends with "="')
            continue
        debug(len(text))

    if not DEBUG:
        print(text.decode('ascii'))
