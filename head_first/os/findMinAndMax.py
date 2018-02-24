#!/usr/bin/env python
# -*- coding: utf-8 -*-


def find_min_and_max(l):
    if len(l) == 0:
        return None, None
    min_item = l[0]
    max_item = l[0]
    for item in l:
        if item < min_item:
            min_item = item
        if item > max_item:
            max_item = item
    return min_item, max_item


un_sorted_list = [2, 1, 4, 56, 67, 7, 32, 2, 43, 1, 4, 2]
sorted_tuple = find_min_and_max(un_sorted_list)
print(sorted_tuple)
print(type(sorted_tuple))
print(sorted_tuple.__class__)
