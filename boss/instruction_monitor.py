#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging

import cx_Oracle
import requests
import schedule

INTERVAL = 30

DEAL_STATUS = 'dealStatus'

APPLICATION_JSON = 'application/json'

CONTENT_TYPE = 'Content-Type'

SEND_MESSAGE_URL = 'http://58.87.84.167:5000/send-message'

FIND_ALL_URL = 'https://op.stariboss.com/message-center-service/send-message/all'

GROUP_NAME = '新BOSS告警'

HOST = 'starboss.csxbifqn7nwb.eu-west-1.rds.amazonaws.com'
PORT = '1521'
SID = 'STARBOSS'
USER = 'boss_query'
PASSWORD = '!@#'

SEND_NOT_RECEIVE_SQL = 'SELECT company_id,count(id) FROM BOSS_PMS_PARTITION.EQUIPMENT_INSTRUCTION ei where ei.STATUS = 1 and ei.DEAL_STATUS in (4, 6) and ei.LAST_SEND_INSTANT < sysdate - 1/24 GROUP BY company_id'

dsn = cx_Oracle.makedsn(HOST, PORT, SID)
dsn_tns = dsn.replace('SID', 'SERVICE_NAME')


def monitor():
    try:
        conn = cx_Oracle.connect(USER, PASSWORD, dsn_tns)
        handle_send_not_receive_message(conn)
        conn.close()
    except Exception as e:
        logging.exception(e)


def handle_send_not_receive_message(conn):
    not_receive_cursor = conn.cursor()
    not_receive_cursor.execute(SEND_NOT_RECEIVE_SQL)
    company_count_tuple = not_receive_cursor.fetchall()
    if company_count_tuple:
        message_content = '\n'.join(['公司%s存在%s条长时间未处理的指令' % (x[0], x[1]) for x in company_count_tuple])
        send_fail_message(message_content)


def send_fail_message(content):
    logging.error(content)
    data = {"content": content}
    headers = {CONTENT_TYPE: APPLICATION_JSON}
    requests.post(url=SEND_MESSAGE_URL, data=json.dumps(data), headers=headers)


monitor()
schedule.every(INTERVAL).minutes.do(monitor)
logging.warning('instruction monitor start')
while True:
    schedule.run_pending()
