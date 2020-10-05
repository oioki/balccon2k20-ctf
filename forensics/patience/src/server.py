#!/usr/bin/env python3

import time

from flask import Flask, request, make_response

from flag import FLAG

DELAY = 0.500

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-',
                   '_': "", '{': "", '}': ""}

morse_code = ''
for char in FLAG:
    morse_code += MORSE_CODE_DICT[char.upper()]
    morse_code += ' '

print(morse_code)

app = Flask(__name__)


sequence = {}


def response(delay=0):
    time.sleep(delay)
    resp = make_response('OK')
    resp.headers['Server'] = 'Boring Server 1.0'
    return resp


@app.route('/')
def index():
    ip = request.remote_addr


    if ip not in sequence:
        sequence[ip] = 0

    if sequence[ip] > len(morse_code) - 1:
        return response(2*DELAY)

    code = morse_code[sequence[ip]]
    sequence[ip] += 1

    if code == '.':
        return response()

    if code == '-':
        return response(DELAY)

    # code == ' '
    return response(2*DELAY)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
