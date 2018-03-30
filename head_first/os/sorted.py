#!/usr/bin/env python
# -*- coding: utf-8 -*-
data = [5, 6, -7, 8, 2, -1, 1, 2, 4]
new_data = sorted(data)
print(data)
print(new_data)

print(sorted(data, key=abs))

words = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(words))
print(sorted(words, key=str.lower))
print(sorted(words, key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]


L3 = sorted(L, key=by_score, reverse=True)
print(L3)