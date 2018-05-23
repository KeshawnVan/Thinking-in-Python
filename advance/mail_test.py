#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.header import Header
from email.mime.text import MIMEText

import advance.mail

sender = 'fankx@startimes.com.cn'

receivers = ['fankx@startimes.com.cn']

email_message = MIMEText('message center ', 'utf-8')
email_message['From'] = Header("message center alerting", 'utf-8')
email_message['To'] = Header(str(receivers), 'utf-8')
subject = 'message center alerting'
email_message['Subject'] = Header(subject, 'utf-8')

advance.mail.send_email(sender, receivers, email_message)
