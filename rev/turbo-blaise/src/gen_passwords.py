#!/usr/bin/env python3

# http://edoceo.com/utilitas/mnemonic-password-generator

secret_string = 'lifeisnotaproblemtobesolved'


def xor(s):
    output = []
    s = s.strip()
    s = s + ' ' * (24 - len(s))
    for i in range(24):
        output.append(str(ord(s[i]) ^ ord(secret_string[i])))
    print('(* {} *)'.format(s))
    print('(' + ','.join(output) + ')', end='')


f = open('passwords.txt', 'r')
lines = f.readlines()
for line in lines[:-1]:
    xor(line)
    print(',')

xor(lines[-1])
