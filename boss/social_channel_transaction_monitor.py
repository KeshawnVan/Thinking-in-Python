#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 检测最近一天，社会渠道交易记录修改时间和创建时间差值超过五分钟的数据

import json
import time
import logging

import cx_Oracle
import requests
import schedule

TIME_STR = "00:00"

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

SQL = 'SELECT CEIL( EXTRACT( SECOND FROM ( s.MODIFY_INSTANT - s.CREATE_INSTANT ) ) ), count( id )  FROM BOSS_COLLECTION.SOCIAL_CHANNEL_TRANSACTION s WHERE DATA_SOURCE_TYPE = 0 AND EXTRACT( SECOND FROM ( s.MODIFY_INSTANT - s.CREATE_INSTANT ) ) > 5 AND s.CREATE_INSTANT > sysdate - 1 GROUP BY CEIL( EXTRACT( SECOND FROM ( s.MODIFY_INSTANT - s.CREATE_INSTANT ) ) ) ORDER BY CEIL( EXTRACT( SECOND FROM ( s.MODIFY_INSTANT - s.CREATE_INSTANT ) ) )'

dsn = cx_Oracle.makedsn(HOST, PORT, SID)
dsn_tns = dsn.replace('SID', 'SERVICE_NAME')


def monitor():
    try:
        conn = cx_Oracle.connect(USER, PASSWORD, dsn_tns)
        cursor = conn.cursor()
        cursor.execute(SQL)
        data = cursor.fetchall()
        if data:
            logging.warning(data)
            send_fail_message(data)
        else:
            logging.warning('no error data')
        cursor.close()
        conn.close()
    except Exception as e:
        logging.exception(e)
        time.sleep(100)
        monitor()


def send_fail_message(data):
    content = '社会渠道交易记录表存在耗时过长的数据: \n %s' % '\n '.join(['耗时%s秒的有%s条数据' % (x[0], x[1]) for x in data])
    logging.error(content)
    data = {"content": content}
    headers = {CONTENT_TYPE: APPLICATION_JSON}
    requests.post(url=SEND_MESSAGE_URL, data=json.dumps(data), headers=headers)


monitor()
schedule.every().day.at(TIME_STR).do(monitor)
logging.warning('social channel transaction monitor start')
while True:
    schedule.run_pending()
