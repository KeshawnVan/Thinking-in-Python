#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times


searah = Athlete('fankx', '2018-02-11', ['2:58', '2:57'])
print(searah.name)
print(searah.times)
