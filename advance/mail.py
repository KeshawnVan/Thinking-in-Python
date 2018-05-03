#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib


email_host = 'smtp.startimes.com.cn'
email_port = 25
email_user = 'fankx@startimes.com.cn'
email_pass = 'Fkx1472580'

smtpObj = smtplib.SMTP()
smtpObj.connect(email_host, email_port)
smtpObj.login(email_user, email_pass)


def send_email(sender, receivers, message):
    try:
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


