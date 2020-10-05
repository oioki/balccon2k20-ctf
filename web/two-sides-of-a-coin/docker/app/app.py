#!/usr/bin/env python3

import datetime
import os
import string
import random
import time

import sqlite3

from flask import Flask, redirect, render_template, request, url_for

READONLY = False
if os.getenv('READONLY'):
    READONLY = bool(os.getenv('READONLY'))


app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('board.db')
    c = conn.cursor()
    c.execute('SELECT id_viewer, title FROM board')

    data = []
    for item in c.fetchall():
        data.append({
            'id': item[0],
            'title': item[1],
        })
    conn.close()

    return render_template('index.html', data=data, readonly=READONLY)


def get_random_id():
    alphabet = list(string.ascii_lowercase + string.digits)

    return ''.join([random.choice(alphabet) for _ in range(32)])


@app.route('/add', methods=['GET', 'POST'])
def add():
    if READONLY:
        return 'Sorry, new advertisements are temporarily not allowed.'

    if request.method == 'GET':
        return render_template('add.html')

    posted_at = round(time.time(), 4)
    random.seed(posted_at)
    id_viewer = get_random_id()
    id_editor = get_random_id()

    conn = sqlite3.connect('board.db')
    c = conn.cursor()
    params = (id_viewer, id_editor, posted_at, request.form['title'], request.form['text'], request.form['text_extra'])
    c.execute('INSERT INTO board VALUES (?, ?, ?, ?, ?, ?)', params)
    conn.commit()
    conn.close()

    return redirect('/view/' + id_editor)


@app.route('/view/<_id>')
def view(_id):
    conn = sqlite3.connect('board.db')
    c = conn.cursor()
    params = (_id, _id)
    c.execute('SELECT id_viewer, id_editor, posted_at, title, text_viewer, text_editor FROM board WHERE id_viewer = ? OR id_editor = ? LIMIT 1', params)
    data = c.fetchone()

    if not data:
        return 'Advertisement not found.', 404

    # extra notes for editor
    is_editor = (data[1] == _id)
    text_extra = None
    url_viewer = None

    if is_editor:
        text_extra = data[5]
        url_viewer = url_for('view', _id=data[0])

    data = {
        'posted_at': datetime.datetime.fromtimestamp(data[2], tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'title': data[3],
        'text': data[4],
        'text_extra': text_extra,
        'url_viewer': url_viewer,
    }
    conn.close()

    return render_template('view.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
