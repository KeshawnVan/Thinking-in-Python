#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import requests
import schedule
import cx_Oracle

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
PASSWORD = ''

COUNT_SQL = 'select count(id) from BOSS_MESSAGE_CENTER.SEND_MESSAGE where deal_status = 2 and failure_count = 5 and status = 1'
DETAIL_SQL = 'select id,company_id,create_instant from BOSS_MESSAGE_CENTER.SEND_MESSAGE where deal_status = 2 and failure_count = 5 and status = 1'
SEND_NOT_RECEIVE_SQL = 'SELECT company_id,count(id) FROM BOSS_MESSAGE_CENTER.SEND_MESSAGE m where m.STATUS = 1 and m.DEAL_STATUS = 4 and m.LAST_SEND_INSTANT < sysdate - 1/24 GROUP BY company_id'

dsn = cx_Oracle.makedsn(HOST, PORT, SID)
dsn_tns = dsn.replace('SID', 'SERVICE_NAME')


def monitor():
    try:
        conn = cx_Oracle.connect(USER, PASSWORD, dsn_tns)

        handle_failure_message(conn)

        handle_send_not_receive_message(conn)
        conn.close()
    except Exception as e:
        logging.exception(e)


def handle_send_not_receive_message(conn):
    not_receive_cursor = conn.cursor()
    not_receive_cursor.execute(SEND_NOT_RECEIVE_SQL)
    company_count_tuple = not_receive_cursor.fetchall()
    if company_count_tuple:
        message_content = '\n'.join(['公司%s存在%s条长时间已发送未返回的消息' % (x[0], x[1]) for x in company_count_tuple])
        send_fail_message(message_content)


def handle_failure_message(conn):
    cursor = conn.cursor()
    cursor.execute(COUNT_SQL)
    count = cursor.fetchone()[0]
    logging.warning('find %s fail messages' % count)
    cursor.close()
    if count > 10:
        detail = get_detail(conn)
        content = 'message center has %s send failure messages, detail is %s' % (count, detail)
        send_fail_message(content)


def get_detail(conn):
    detail_cursor = conn.cursor()
    detail_cursor.execute(DETAIL_SQL)
    all_message = detail_cursor.fetchall()
    detail = ''
    detail_cursor.close()
    for message in all_message:
        detail += "[id : %s companyId: %s createTime: %s] " % (message[0], message[1], message[2])
    logging.warning('fail_messages is %s' % detail)
    return detail


def send_fail_message(content):
    logging.error(content)
    data = {"content": content}
    headers = {CONTENT_TYPE: APPLICATION_JSON}
    requests.post(url=SEND_MESSAGE_URL, data=json.dumps(data), headers=headers)


monitor()
schedule.every(INTERVAL).minutes.do(monitor)
logging.warning('message center monitor start')
while True:
    schedule.run_pending()
