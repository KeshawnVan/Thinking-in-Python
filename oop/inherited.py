#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    def run(self):
        print('Dog is running')

    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(dog, Animal))
print(isinstance(dog, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(dog)
