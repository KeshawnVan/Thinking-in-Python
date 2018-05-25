#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cx_Oracle

HOST = 'starboss.csxbifqn7nwb.eu-west-1.rds.amazonaws.com'
PORT = '1521'
SID = 'STARBOSS'
USER = 'boss_query'
PASSWORD = '%%^'

dsn = cx_Oracle.makedsn(HOST, PORT, SID)
dsn_tns = dsn.replace('SID', 'SERVICE_NAME')
conn = cx_Oracle.connect(USER, PASSWORD, dsn_tns)

sql = 'select id,company_id,create_instant from BOSS_MESSAGE_CENTER.SEND_MESSAGE where deal_status = 1'

cursor = conn.cursor()

cursor.execute(sql)

all_message = cursor.fetchall()

detail = ''
for message in all_message:
    detail += "[id : %s companyId: %s createTime: %s] " % (message[0], message[1], message[2])

print(detail)
cursor.close()
conn.close()
