#!/usr/bin/env python3

import os
from PIL import Image


OFFSET = 60
SIDE = 90


PIECE_PATTERNS = {
    '.................................##################################.......................': '',   # pawn
    '...............................####################################.......................': 'K',  # king
    '..............................################################........########............': 'B',  # bishop
    '...........................#########...###############################....................': 'Q',  # queen black
    '..........................##########...###############################....................': 'Q',  # queen white
    '........................######################################################............': 'N',  # knight
    '....................################################################..####................': 'R',  # rook
}


def get_piece_type(pixels, y, x):
    pattern = ''
    for z in range(SIDE):
        if pixels[y+z][x+z] in [48, 58]:
            pattern += '.'
        else:
            pattern += '#'
    return PIECE_PATTERNS[pattern]


def print_move(pixels):
    piece = ''
    from_position = None
    to_position = None
    for i in range(8):
        for j in range(8):
            x = j*SIDE
            y = OFFSET+i*SIDE
            if pixels[y][x] in [48, 58]:
                position = '{}{}'.format(chr(ord('a') + j), 8-i)
                if pixels[y+SIDE//2][x+SIDE//2] not in [48, 58]:
                    piece = get_piece_type(pixels, y, x)
                    to_position = position
                else:
                    from_position = position
    print('{}{}{}'.format(piece, from_position[0], to_position), end=' ')


def print_game(in_gif):
    frame = Image.open(in_gif)
    nframes = 0
    while frame:
        pixels = list(frame.getdata())
        width, height = frame.size
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

        if nframes % 2 == 1:
            print('{}.'.format((nframes+1) // 2), end=' ')

        if nframes:
            print_move(pixels)

        nframes += 1
        try:
            frame.seek(nframes)
        except EOFError:
            break
    return True


def extract_frames(in_gif, out_folder):
    os.mkdir(out_folder)
    frame = Image.open(in_gif)
    nframes = 0
    while frame:
        frame.save('%s/%s-%03d.gif' % (out_folder, os.path.basename(in_gif), nframes), 'GIF')
        nframes += 1
        try:
            frame.seek(nframes)
        except EOFError:
            break
    return True


# extract_frames('../challenge/noob-game.gif', 'output')
print_game('../challenge/noob-game.gif')
