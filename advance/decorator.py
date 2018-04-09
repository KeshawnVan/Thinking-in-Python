#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
import time


def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def now():
    print('2018-04-09')


f = now
f()
print(now.__name__)
print(f.__name__)


def custom_log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@custom_log('execute')
def fishing():
    print('fishing')


fishing()


def get_time():
    return int(round(time.time() * 1000))


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = get_time()
        time.sleep(0.0022)
        result = func(*args, **kwargs)
        print('%s executed in %s ms' % (func.__name__, get_time() - start))
        return result

    return wrapper


@metric
def new_fishing():
    print('new fishing')


new_fishing()


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
