#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging

import requests
import schedule

INTERVAL = 10

DEAL_STATUS = 'dealStatus'

APPLICATION_JSON = 'application/json'

CONTENT_TYPE = 'Content-Type'

SEND_MESSAGE_URL = 'http://58.87.84.167:5000/send-message'

FIND_ALL_URL = 'https://op.stariboss.com/message-center-service/send-message/all'

GROUP_NAME = '新BOSS告警'


def monitor():
    try:
        response = requests.get(FIND_ALL_URL)
        response_json = response.content.decode()
        if response_json is not None:
            messages = json.loads(response_json)
            fail_messages = list(filter(lambda message: message[DEAL_STATUS] == 'SEND_FAILURE', messages))
            logging.warning('fail_messages is %s' % fail_messages)
            fail_message_length = len(fail_messages)
            if fail_message_length > 10:
                send_fail_message(fail_message_length, fail_messages)
    except Exception as e:
        logging.exception(e)


def send_fail_message(fail_message_length, fail_messages):
    content = 'message center has %s send failure messages, company is %s' % (
        fail_message_length, set([message['companyId'] for message in fail_messages]))
    logging.error(content)
    data = {"receiver": GROUP_NAME, "content": content}
    headers = {CONTENT_TYPE: APPLICATION_JSON}
    requests.post(url=SEND_MESSAGE_URL, data=json.dumps(data), headers=headers)


schedule.every(INTERVAL).minutes.do(monitor)
while True:
    schedule.run_pending()
