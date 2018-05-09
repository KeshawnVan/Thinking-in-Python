#!/usr/bin/env python
# -*- coding: utf-8 -*-
import types

print(type(123))

print(abs)

print(type(123) == type(456))
print(type(123) == int)


def my_fun():
    print('nothing')


print(type(my_fun) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print(isinstance(type((x for x in range(10))), types.GeneratorType))

print(dir('ABC'))


class MyDog(object):
    def __init__(self):
        self.x = 9

    def __len__(self):
        return 100


dog = MyDog()
dog.z = 2
print(len(dog))
print(hasattr(dog, 'x'))
print(hasattr(dog, 'z'))
print(hasattr(dog, 'y'))
setattr(dog, 'y', 1)
print(hasattr(dog, 'y'))
print(dog.y)

print(getattr(dog, 'q', 404))

print(dog.w)
