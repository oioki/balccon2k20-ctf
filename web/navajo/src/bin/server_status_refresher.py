#!/usr/bin/env python3

import threading
import time
import random
import requests


BASE_URL = 'http://localhost'

PATHS = [
    "index.html",
    "favicon.ico",
    "flag.txt",
    "robots.txt",
    "404",
    "burek.jpg",
    "flowers.jpg",
    "kittens.jpg",
]

PATH_FLAG = 'BCTF{extremely_secret_url_no_one_can_guess}'


def fetch(paths, interval):
    while True:
        time.sleep(interval)

        path = random.choice(paths)
        headers = {"Connection": "close"}

        try:
            r = requests.get(BASE_URL + '/' + path, headers=headers)
            #print(r.status_code, path)
        except:
            pass


if __name__ == '__main__':
    t1 = threading.Thread(target=fetch, args=(PATHS, 0.01))
    t2 = threading.Thread(target=fetch, args=([PATH_FLAG], 20.0))

    t1.start()
    t2.start()
