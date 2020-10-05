#!/usr/bin/env python3

import random
import time

import requests


DELAY_MAX = 10.0
#DELAY_MAX = 1.0

URL = 'http://poc.nuke.tk/'
#URL = 'http://localhost:80/'

headers = {
    'User-Agent': 'Boring Client 1.0',
}

long_responses = 0

while True:
    t1 = time.time()
    r = requests.get(URL, headers=headers)
    t2 = time.time()
    print(round(t2-t1, 2), r.text)
    if t2-t1 > 1.0:
        long_responses += 1
    else:
        long_responses = 0
    if long_responses == 3:
        exit()

    time.sleep(DELAY_MAX * random.random())
