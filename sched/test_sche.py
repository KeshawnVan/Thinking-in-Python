#!/usr/bin/env python
# -*- coding: utf-8 -*-
import schedule
import time


def p():
    print(time.time())


schedule.every().day.at("11:07").do(p)

while True:
    schedule.run_pending()