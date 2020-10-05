#!/usr/bin/env python3

import subprocess


f = open('game2.txt', 'r')
s = f.read()
f.close()

parts = s.split()
for i in range(len(parts), 0, -3):
    game = ' '.join(parts[:i])
    print(game)
    subprocess.call(['chess-steg', '-w', '-u', game])
    print()
