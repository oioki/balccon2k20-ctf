#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Šatrovački#Utrovački

parts = [
    ('bez',),
    ('mu', 'zike'),
    ('zi', 'vot'),
    ('bi',),
    ('bi', 'o'),
    ('jed', 'na'),
    ('ve', 'lika'),
    ('gres', 'ka'),
]


def utrovacki(part):
    if len(part) == 2:
        return 'u{}za{}nje'.format(part[1], part[0])

    return part[0]



if __name__ == '__main__':
    cipherparts = []

    for part in parts:
        cipherparts.append(utrovacki(part))

    output = utrovacki(('b', 'ctf')) + '{' + '_'.join(cipherparts) + '}'
    print(output[::-1])
