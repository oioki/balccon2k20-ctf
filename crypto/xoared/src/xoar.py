#!/usr/bin/env python3

import os


LEN_KEY = 43

f = open('flag.txt', 'rb')
flag = f.read()
f.close()


def xor(s1, s2):
    result = bytearray(b'\x00' * len(s1))

    for i in range(len(s1)):
        result[i] = s1[i] ^ s2[i % len(s2)]

    return result


def make_key_producing_hint(len_key, hint_offset, hint_string):
    left = os.urandom(hint_offset)
    center = xor(hint_string, flag[hint_offset:hint_offset + len(hint_string)])
    right = os.urandom(len_key - hint_offset - len(hint_string))
    return left + center + right


if __name__ == '__main__':
    #key = os.urandom(LEN_KEY)
    key = make_key_producing_hint(len_key=LEN_KEY, hint_offset=16, hint_string=b'{factors?}')

    plaintext = flag * LEN_KEY

    ciphertext = xor(plaintext, key)

    f = open('../challenge/xoared', 'wb')
    f.write(ciphertext)
    f.close()
