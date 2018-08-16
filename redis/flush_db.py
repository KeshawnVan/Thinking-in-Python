#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import schedule

r = redis.Redis(host="10.0.251.210", port=30203, decode_responses=True, db=1)

# r.flushdb()

# r.hset("pms_center:equipment", '10001', equipment)

def fresh():
    r.hset("pms_center:equipment", '123', equipment)


equipment = r.hget("pms_center:equipment", '123')
schedule.every(10).seconds.do(fresh)
while True:
    schedule.run_pending()
