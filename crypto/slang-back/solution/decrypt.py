#!/usr/bin/env python3

import re

f = open('../challenge/slang-back.txt', 'r')
s = f.read().strip()
f.close()

flag = ''

parts = re.split('[}{_]', s[::-1])
for part in parts:
    part_parts = part.split('za')
    if len(part_parts) == 1:
        flag += part
    else:
        flag += part_parts[1].replace('nje', '')
        flag += part_parts[0].replace('u', '')
    flag += ' '

print(flag)
