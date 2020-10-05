#!/usr/bin/env python3

import calendar
import random
import time

# Hack but I did not want to copypaste `get_random_id` method
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir + '/docker/app')

from app import get_random_id


DATE = '2020-09-22'

timestamp_0 = calendar.timegm(time.strptime(DATE + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
timestamp = timestamp_0
while timestamp < timestamp_0 + 24*3600:
    random.seed(timestamp)
    id_viewer = get_random_id()
    print(timestamp, id_viewer)
    timestamp = round(timestamp + 0.0001, 4)
