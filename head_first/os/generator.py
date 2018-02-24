#!/usr/bin/env python
# -*- coding: utf-8 -*-
first_generator = (x * x for x in range(1, 100))
print(next(first_generator))
for i in first_generator:
    print(i)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print([x for x in f])
