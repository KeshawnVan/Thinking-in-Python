#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests
import schedule

INTERVAL = 30

GROUP_NAME = 'WXDEV'

APPLICATION_JSON = 'application/json'

CONTENT_TYPE = 'Content-Type'

SEND_MESSAGE_URL = 'http://58.87.84.167:5000/send-message'


def check():
    message = {'receiver': GROUP_NAME, 'content': 'heartbeat'}
    headers = {CONTENT_TYPE: APPLICATION_JSON}
    requests.post(url=SEND_MESSAGE_URL, data=json.dumps(message), headers=headers)


schedule.every(INTERVAL).seconds.do(check)

while True:
    schedule.run_pending()
