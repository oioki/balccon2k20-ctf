#!/usr/bin/env python3

import pyshark


DELAY_THRESHOLD = 0.5


cap = pyshark.FileCapture('../challenge/patience.pcap', use_json=True)

stream_count = {}

i = 0

morse_code = ''

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
                   ' ': ""}

REVERSE_MORSE_CODE_DICT = {}

for character in MORSE_CODE_DICT:
    code = MORSE_CODE_DICT[character]
    REVERSE_MORSE_CODE_DICT[code] = character


for pkt in cap:
    if 'HTTP' in pkt:
        # print(pkt['HTTP'])
        if 'time' in str(pkt['HTTP']):
            response_time = float(pkt['HTTP'].time)
            if response_time > 2*DELAY_THRESHOLD:
                morse_code += ' '
            elif response_time > DELAY_THRESHOLD:
                morse_code += '-'
            else:
                morse_code += '.'

print(morse_code)

flag = ''
for code in morse_code.split(' '):
    flag += REVERSE_MORSE_CODE_DICT[code]

print(flag)
