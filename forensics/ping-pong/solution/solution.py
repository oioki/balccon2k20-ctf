#!/usr/bin/env python3

import binascii
import pyshark

from crack_password import crack_password


cap = pyshark.FileCapture('../challenge/pingpong.pcap')

stream_count = {}

i = 0

for pkt in cap:
    data = binascii.unhexlify(pkt['ICMP'].data)

    if i == 5:
        challenge = data[5:]
    if i == 6:
        target_digest = data[5:]

    if len(data) > 50:
        c = pyshark.InMemCapture()
        offset = 5  # magic word
        ethernet_header = b'\x00'*12 + b'\x08' + b'\x00'

        pkt_inner = c.parse_packet(ethernet_header + data[offset:])
        print(pkt_inner)
        if 'ICMP' in pkt_inner:
            print(binascii.unhexlify(pkt_inner['ICMP'].data))
        print('-'*100)

    i += 1

password = crack_password(challenge, target_digest)
print('Password was "{}"'.format(password))
