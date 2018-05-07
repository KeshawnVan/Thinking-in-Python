#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
minutes = [5, 6, 7, 8, 2, 1, 1, 2, 4]
seconds = [m * 60 for m in minutes]
print(seconds)
logging.warning('test')
s = '\n'.join([str(x) for x in minutes])
print(s)
