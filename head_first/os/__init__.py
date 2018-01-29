#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def pwd():
    print(os.getcwd())


pwd()
os.chdir('../../../../IdeaProjects/origin')
pwd()
os.chdir('C:/Users/Administrator/Documents/Tencent Files/153523081/FileRecv')
pwd()
os.chdir('C:/Users/Administrator/IdeaProjects/origin')
pwd()
pom = open('pom.xml')
print(pom.readline(), end='')
print(pom.readline(), end='')
pom.seek(0)
for line in pom:
    print(line)
print(pom.name)
pom.close()
os.chdir('C:/Users/Administrator/IdeaProjects/origin')
