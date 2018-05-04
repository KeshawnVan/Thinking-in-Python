#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

FIND_ALL_URL = 'https://op.stariboss.com/message-center-service/send-message/all'

print(requests.get(FIND_ALL_URL))