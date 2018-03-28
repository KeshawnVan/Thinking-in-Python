#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce


def fn(total, current):
    return total * 10 + current


g_list = [x for x in range(1, 11)]
result = reduce(fn, g_list)
print(result)


def prod(L):
    return reduce(lambda total, current: total * current, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')