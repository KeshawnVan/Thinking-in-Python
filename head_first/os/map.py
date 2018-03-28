#!/usr/bin/env python
# -*- coding: utf-8 -*-


def f(x):
    return x * x


g_list = [x for x in range(1, 11)]
print(g_list)
map_list = map(f, g_list)
print(list(map_list))


def normalize(name):
    if len(name) != 0:
        return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT', 'a', '']
L2 = list(map(normalize, L1))
print(L2)
