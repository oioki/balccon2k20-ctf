#!/usr/bin/env python3

import datetime
import random
import sqlite3


# Hack but I did not want to copypaste `get_random_id` method
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir + '/docker/app')

from app import get_random_id


DATE = '2020-09-22'


epoch = datetime.datetime.utcfromtimestamp(0)

def unixtime(dt):
    return (dt - epoch).total_seconds()


def add_entry(entry):
    time_string = DATE + ' ' + entry['time']
    posted_at = unixtime(datetime.datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S.%f'))
    random.seed(posted_at)
    id_viewer = get_random_id()
    id_editor = get_random_id()

    params = (id_viewer, id_editor, posted_at, entry['title'], entry['text'], entry['text_extra'])
    c.execute('INSERT INTO board VALUES (?, ?, ?, ?, ?, ?)', params)


if __name__ == '__main__':
    conn = sqlite3.connect('../docker/app/board.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS board')
    c.execute("""CREATE TABLE board (
  id_viewer VARCHAR(16) PRIMARY KEY,
  id_editor VARCHAR(16),
  posted_at FLOAT,
  title VARCHAR(64),
  text_viewer TEXT,
  text_editor TEXT
);
""")

    entries = [
        {
            'time': '00:00:00.0000',
            'title': 'Buying insomnia pills',
            'text': "I can't sleep anymore. Does anyone have insomnia pills? I can drive to your place right now if needed.",
            'text_extra': 'I am tired, so posting this exactly at midnight.',
        },
        {
            'time': '00:00:33.3333',
            'title': 'Selling PlayStation 4',
            'text': 'Price $500.',
            'text_extra': 'Bought it previously for $400 :-)',
        },
        {
            'time': '00:07:33.7937',
            'title': 'Selling baby toys',
            'text': "My son grown up, so I don't need some toys anymore. Come and see.",
            'text_extra': "Let's see how much I can get from it.",
        },
        {
            'time': '04:25:06.3345',
            'title': 'All for $1',
            'text': "Come to my backyard and check yourself.",
            'text_extra': "URL looks interesting indeed. However, the flag is not here.",
        },
        {
            'time': '09:00:00.0000',
            'title': 'Not selling anything, just kidding',
            'text': 'Look how cool I am. Posted this exactly at 9 a.m.',
            'text_extra': '(Like a boss)',
        },
        {
            'time': "13:37:10.1010",
            'title': "Buying digital piano",
            'text': "Yamaha or similar.",
            'text_extra': "You're on the right track.",
        },
        {
            'time': "14:12:12.9998",
            'title': "Selling Ferrari",
            'text': "105,000 EUR -- for the same price I bought it before.",
            'text_extra': "It's too cool for me.",
        },
        {
            'time': "20:09:39.1234",
            'title': "Cargo delivering",
            'text': "Any time, any weight, anywhere!",
            'text_extra': "Almost there, mate...",
        },
        {
            'time': "21:09:31.3371",
            'title': "Will code for food",
            'text': "If you're interested, drop me a message.",
            'text_extra': "BCTF{numb3rs_from_PRNG_are_n0t_really_rand0m}",
        },
        {
            'time': "23:59:59.9999",
            'title': "Still buying insomnia pills",
            'text': "Anyone? Please help.",
            'text_extra': "It is the end! Flag should be somewhere earlier.",
        },

    ]

    for entry in entries:
        add_entry(entry)

    conn.commit()
    conn.close()
