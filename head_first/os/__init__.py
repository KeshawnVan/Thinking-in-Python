#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def pwd():
    print(os.getcwd())


pwd()
os.chdir("../..")
pwd()
pom = open('README.md')
print(pom.readline(), end='')
pom.seek(0)
for line in pom:
    print(line)
print(pom.name)
pom.close()
