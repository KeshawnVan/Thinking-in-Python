#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests
from flask import Flask
from flask import request

app = Flask(__name__)


class Config(object):
    def __init__(self, corp_id, agent_id, secret, token):
        self.corp_id = corp_id
        self.agent_id = agent_id
        self.secret = secret
        self.token = token


CORP_ID = ""

AGENT_ID = 1000025

SECRET = ""

APPLICATION_JSON = 'application/json'

CONTENT_TYPE = 'Content-Type'

access_token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s" % (CORP_ID, SECRET)

send_message_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s"


def get_token():
    return json.loads(requests.get(access_token_url).text).get("access_token")


token = get_token()

config = Config(CORP_ID, AGENT_ID, SECRET, token)


def send_message(content):
    post_url = send_message_url % config.token
    message = {
        "touser": "@all",
        "toparty": "",
        "totag": "",
        "msgtype": "text",
        "agentid": AGENT_ID,
        "text": {
            "content": content
        },
        "safe": 0
    }
    response = requests.post(url=post_url, data=json.dumps(message))
    error_code = json.loads(response.text).get('errcode')
    if error_code == 40014 or error_code == 42001 or error_code == 42007 or error_code == 42009:
        new_token = get_token()
        config.token = new_token
        send_message(content)


@app.route('/send-message', methods=['post', 'get'])
def send():
    message = request.json
    if message is not None and message.get('content') is not None:
        send_message(message.get('content'))
        return '<h3>send wechat message success.</h3>'
    else:
        return '<h3>param cannot be null.</h3>'


if __name__ == '__main__':
    app.run(host='172.21.0.13', port=5000, debug=True)
