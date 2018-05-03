#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name, score, sex):
        self.name = name
        self.score = score
        self.__sex = sex

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex


young_man = Student("ha", 1, "man")
print(young_man)

young_man.name = "fkx"
print(young_man.name)

nana = Student("nana", 100, "woman")
print(nana)
print(nana.name)

nana.print_score()
print(nana.get_sex())
nana.set_sex("girl")


# warn
nana.__sex = "error"
print(nana.__sex)

nana.set_sex('my girl')