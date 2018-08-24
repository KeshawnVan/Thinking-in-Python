#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Student(object):
    pass


s = Student()
s.name = 'Mike'
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
s2.set_age(25)


def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)


class SlotsStudent(object):
    __slots__ = ('name', 'age')


ss = SlotsStudent()
ss.name = 'Jack'
ss.age = 11
ss.score = 20


# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class GraduateStudent():
    pass


g = GraduateStudent()
g.score = 1000
print(g.score)


class PropertyStudent(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


ps = PropertyStudent()
ps.score = 60
print(ps.score)
ps.score = 9999


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
sc = Screen()
sc.width = 1024
sc.height = 768
print('resolution =', sc.resolution)
if sc.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
