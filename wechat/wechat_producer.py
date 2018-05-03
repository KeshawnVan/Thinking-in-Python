#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika

import json

# 认证
credentials = pika.PlainCredentials("guest", "guest")

# 连接参数
conn_params = pika.ConnectionParameters("58.87.84.167", credentials=credentials)

# 创建连接
conn_broker = pika.BlockingConnection(conn_params)

# 获取channel
channel = conn_broker.channel()

# 声明交换器
channel.exchange_declare(exchange="wechat-exchange", exchange_type='direct', passive=False, durable=True,
                         auto_delete=False)

# 获取消息
message_dto = {'receiver': '比利外卖', 'content': '3 country kill'}
msg = json.dumps(message_dto)

# 设置消息参数
msg_props = pika.BasicProperties(delivery_mode=2)
msg_props.content_type = "text/plain"

# 发送方确认模式处理器
# def confirm_handler(frame):
#     if type(frame.method) == spec.Basic.Ack:
#         if frame.method.delivery_tag in msg_ids:
#             print("Confirm received!")
#             msg_ids.remove(frame.method.delivery_tag)
#     elif type(frame.method) == spec.Basic.Nack:
#         if frame.method.delivery_tag in msg_ids:
#             print("Message lost")
#     elif type(frame.method) == spec.Confirm.SelectOk:
#         print("Channel in confirm mode")


# 设置为confirm模式
channel.confirm_delivery()

# 发送消息
result = channel.basic_publish(body=msg, exchange="wechat-exchange", properties=msg_props, routing_key="wechat")

# 打印发送结果
print(result)

# 关闭channel
channel.close()
