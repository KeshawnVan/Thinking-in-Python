#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pika
from flask import Flask
from flask import request

app = Flask(__name__)

# 认证
credentials = pika.PlainCredentials("guest", "guest")

# 连接参数
conn_params = pika.ConnectionParameters("172.21.0.13", credentials=credentials, heartbeat_interval=0)


@app.route('/send-message', methods=['post', 'get'])
def hello():
    message = request.json
    if message is not None and message.get('receiver') is not None and message.get('content') is not None:
        # 创建连接
        conn_broker = pika.BlockingConnection(conn_params)

        # 获取channel
        channel = conn_broker.channel()

        # 声明交换器
        channel.exchange_declare(exchange="wechat-exchange", exchange_type='direct', passive=False, durable=True,
                                 auto_delete=False)

        # 设置消息参数
        msg_props = pika.BasicProperties(delivery_mode=2)
        msg_props.content_type = "text/plain"

        channel.basic_publish(body=json.dumps(message), exchange="wechat-exchange", properties=msg_props,
                              routing_key="wechat")
        return '<h3>send wechat message success.</h3>'
    else:
        return '<h3>param cannot be null.</h3>'


if __name__ == '__main__':
    app.run(host='172.21.0.13', port=5000, debug=True)
