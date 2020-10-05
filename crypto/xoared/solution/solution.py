#!/usr/bin/env python3


def xor(s1, s2):
    result = bytearray(b'\x00' * len(s1))

    for i in range(len(s1)):
        result[i] = s1[i] ^ s2[i % len(s2)]

    return result


if __name__ == '__main__':
    f = open('../challenge/xoared', 'rb')
    ciphertext = f.read()
    f.close()

    LEN_KEY = 43
    LEN_FLAG = len(ciphertext) // LEN_KEY

    for i in range(LEN_FLAG):
        assert(ciphertext[i] ^ ciphertext[i+LEN_KEY] == ciphertext[i+LEN_FLAG] ^ ciphertext[i+LEN_FLAG+LEN_KEY])


    known_part = b'BCTF{'

    plaintext_solution = ''

    for i in range(LEN_FLAG):
        key = xor(known_part, ciphertext[i:i+len(known_part)])

        plaintext = ''
        for j in range(LEN_FLAG):
            left_side = i + j * LEN_KEY
            right_side = left_side + len(known_part)

            if right_side > len(ciphertext):
                continue

            ciphertext_part = ciphertext[left_side:right_side]
            plaintext_part = xor(ciphertext_part, key).decode('ascii')

            plaintext += plaintext_part + ' '

            if i == 8:
                plaintext_solution += plaintext_part[:2]

        print(i, bytes(plaintext, 'utf-8'))

    print('Solution:', plaintext_solution)
