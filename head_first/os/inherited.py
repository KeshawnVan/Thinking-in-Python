#!/usr/bin/env python
# -*- coding: utf-8 -*-
class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name


johnny = NamedList("a b c")
print(dir(johnny))
johnny.append("l1")
johnny.extend(['l2', 'l3'])
print(johnny)
print(johnny.name)