#!/usr/bin/env python3

import subprocess
import sys

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    ip = request.remote_addr
    info = ''
    content = ''

    url = request.args.get("url")

    args = ['curl', '-s']

    # allow redirect following only for local IP
    if ip == '127.0.0.1':
        info = ' PRIVILEGED MODE ENABLED.'
        args.append('-L')

    if url:
        if not url.startswith('http://'):
            return 'Sorry, only http:// is supported.', 400

        args.append(url)
        res = subprocess.run(args, stdout=subprocess.PIPE)
        content = "".join(map(chr, res.stdout))

    return render_template('index.html', ip=ip, info=info, content=content)


@app.route('/flag')
@app.route('/flag.txt')
def fake_flag():
    return 'Wrong way.'


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
