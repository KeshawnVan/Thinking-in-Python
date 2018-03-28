#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce


def positive_calculate(total, current):
    return total * 10 + current


def minus_calculate(total, current):
    if total == 0:
        return 0.1 * current
    else:
        str_total = str(total)
        index = str_total.find('.')
        length = len(str_total[index + 1:])
        return total + (0.1 * (length + 1))


def str2float(s):
    index = s.find('.')
    return reduce(positive_calculate, map(int, s[0:index])) + reduce(minus_calculate, map(int, s[index + 1:]))


#print(str2float('12.12'))

