#!/usr/bin/env python
# -*- coding: utf-8 -*-


print(list(map(lambda x: x * x, list(range(1, 11)))))

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
