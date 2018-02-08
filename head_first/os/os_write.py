#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def pwd():
    print(os.getcwd())


pwd()
os.chdir("../..")
try:
    store = []
    with open("README.md", "r") as readme:
        for line in readme:
            store.append(line)
    with open("read.txt", "a+") as out:
        for line in store:
            print(line, file=out)
except IOError as err:
    print('File error: ' + str(err))
