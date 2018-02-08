#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle

with open('myData.pickle', 'wb') as my_save_data:
    pickle.dump((1, 2, 'three'), my_save_data)
with open('myData.pickle', 'rb') as my_store_data:
    a_list = pickle.load(my_store_data)
print(a_list)
