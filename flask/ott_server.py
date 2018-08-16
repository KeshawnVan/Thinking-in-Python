#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/ott', methods=['post', 'get'])
def send():
    return "true"


if __name__ == '__main__':
    app.run(host='172.21.0.13', port=5000, debug=True)
