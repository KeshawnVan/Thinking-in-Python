#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

import json

from wxpy import *

# 认证
credentials = pika.PlainCredentials("guest", "guest")

# 连接参数
conn_params = pika.ConnectionParameters("58.87.84.167", credentials=credentials, heartbeat_interval=0)

# 创建连接
conn_broker = pika.BlockingConnection(conn_params)

# 获取channel
channel = conn_broker.channel()

# 声明交换器
channel.exchange_declare(exchange="wechat-exchange", exchange_type="direct", passive=False, durable=True,
                         auto_delete=False)

# 声明队列
channel.queue_declare(queue="wechat-queue", durable=True)

# 绑定
channel.queue_bind(queue="wechat-queue", exchange="wechat-exchange", routing_key="wechat")

bot = Bot(console_qr=True, cache_path=True)


# 创建consumer
def message_consumer(channel, method, header, body):
    try:
        channel.basic_ack(delivery_tag=method.delivery_tag)
        message_json = str(body, 'utf-8')
        message_dto = json.loads(message_json)
        receiver = message_dto['receiver']
        content = message_dto['content']
        print('wechat send message : [%s] to [%s]' % (content, receiver))
        my_friend = bot.groups().search(message_dto['receiver'])[0]
        my_friend.send(message_dto['content'])
    except Exception as e:
        print(e)
    return


# 订阅消费者
channel.basic_consume(message_consumer, queue="wechat-queue", consumer_tag="wechat-consumer")

# 开始消费
channel.start_consuming()
