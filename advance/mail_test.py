#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

from email.header import Header

from email.mime.text import MIMEText

email_host = 'smtp.qq.com'
email_port = 465
email_user = '153523081@qq.com'
email_pass = 'fecxtjqifoudcaie'

smtpObj = smtplib.SMTP_SSL()
print('connect begin')
smtpObj.connect(email_host, email_port)  # 25 为 SMTP 端口号
print('connect end')
smtpObj.login(email_user, email_pass)

sender = '153523081@qq.com'

receivers = ['fankx@startimes.com.cn']

email_message = MIMEText('message center ', 'utf-8')
email_message['From'] = Header("message center alerting", 'utf-8')
email_message['To'] = Header(str(receivers), 'utf-8')
subject = 'message center alerting'
email_message['Subject'] = Header(subject, 'utf-8')


def send_email(sender, receivers, message):
    try:
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("send email success")
    except smtplib.SMTPException:
        print("send email failure")


send_email(sender, receivers, email_message)