#!/usr/bin/env python3

import socket
import time

sock = socket.socket()
sock.connect(('localhost', 1100))

N = 8
MOVE_DELAY = 0.500

a = None

def convert_s_to_a(s):
    a = []
    for i in range(N):
        a.append([])
        for j in range(N):
            a[i].append(int(s[1+i][4+3*j]))
    return a


def print_state(a):
    for i in range(N):
        for j in range(N):
            print(a[i][j], end='')
        print()


s = sock.recv(1024).decode('ascii').split('\n')
a = convert_s_to_a(s)
print_state(a)

while True:
    # remember position before touching
    b = []
    for i in range(N):
        b.append(a[i].copy())

    # actual moves
    for i in range(N):
        for j in range(N):
            if b[i][j] == 1:
                column = chr(ord('a') + j)
                row = str(i + 1)
                sock.send(bytes(column + row + '\n', 'ascii'))
                time.sleep(MOVE_DELAY)

                s = sock.recv(1024).decode('ascii').split('\n')
                print(s[-2])

                a = convert_s_to_a(s)
                print_state(a)
