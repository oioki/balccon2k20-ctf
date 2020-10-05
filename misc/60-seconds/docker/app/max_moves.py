#!/usr/bin/env python3

import random
import sys
import time

from game import Game


# Empirical formula: Max number of moves for NxN board is approximately
# N**2 * (1 + (N-1)/N) = N * N * (N + N -1) / N = N * (2*N-1)

# max_moves(2)  >=   6
# max_moves(4)  >=  28
# max_moves(6)  >=  66
# max_moves(8)  >= 108
# max_moves(10) >= 141
# max_moves(12) >= 205
# max_moves(14) >= 250
# max_moves(16) >= 349


N = int(sys.argv[1])
MAX = 2

a = None


def one_game():
    game = Game()

    moves = 0

    while True:
        # check for solution
        ones = 0
        for i in range(N):
            for j in range(N):
                if game.a[i][j] == 1:
                    ones += 1
        if ones == 0:
            return moves


        # remember position before touching
        b = []
        for i in range(N):
            b.append(game.a[i].copy())


        # actual moves
        for i in range(N):
            for j in range(N):
                if b[i][j] == 1:
                    game.move(i, j)
                    moves += 1



max_m = 0
min_m = 100
while True:
    m = one_game()
    print(m)
    if m > max_m:
        max_m = m
        print('new max:', max_m)
    if m < min_m:
        min_m = m
        print('new min:', min_m)
