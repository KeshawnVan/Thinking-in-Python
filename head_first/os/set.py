#!/usr/bin/env python
# -*- coding: utf-8 -*-
dis = {1, 2, 5, 3, 21, 2, 21, 1, 2, 1}
print(dis)
minutes = [5, 6, 7, 8, 2, 1, 1, 2, 4]
minutes_set = set(minutes)
print(minutes_set)
print(type(minutes_set))
print(type(dis))
companys = set([x * 3 for x in [5, 6, 7, 8, 2, 1, 1, 2, 4]])
print(companys)
print('companyIds : [%s]' % companys)
