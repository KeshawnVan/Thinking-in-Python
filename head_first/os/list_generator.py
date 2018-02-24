#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

range_list = list(range(1, 11))
print(range_list)
for_list = [x * x for x in range(1, 11)]
print(for_list)
for_if_list = [x * x for x in range(1, 11) if x % 2 == 0]
print(for_if_list)
com_list = [m + n for m in 'ABC' for n in 'XYZ']
print(com_list)
all_file_or_dir = [d for d in os.listdir('.')]
print(all_file_or_dir)
dic_map = {'A': 1, 'B': 2, 'C': 3}
for key, value in dic_map.items():
    print(key, ':', value)
key_value_list = [key + ':' + str(value) for key, value in dic_map.items()]
print(key_value_list)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [string.lower() for string in L1 if isinstance(string, str)]
print(L2)