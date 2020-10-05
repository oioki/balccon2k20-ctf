#!/usr/bin/env python3

import collections


f = open('../challenge/twice-cooler.txt', 'r')
s = f.read().strip()
f.close()

d = {}

for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1

print(len(d))

print(collections.OrderedDict(sorted(d.items())))
