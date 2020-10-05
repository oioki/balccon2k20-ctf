#!/usr/bin/env python3

f = open('../challenge/MAIN.EXE', 'rb')
b = bytearray(f.read())
f.close()


secret_string = 'lifeisnotaproblemtobesolved'

for i in range(100):
    offset = 0x6312 + i*24
    length = 24

    # Make all encoded password to be "LIFEISNOTAPROBLEMTOBESOLVED". This way 21 spaces as a password will work.
    for j in range(len(secret_string)):
        b[offset+j] = ord(secret_string[j]) ^ 0x20


f = open('PATCHED.EXE', 'wb')
f.write(b)
f.close()
