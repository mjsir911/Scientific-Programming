#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import math
import collections

__appname__     = ""
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

def timeme(method):
    def wrapper(*args, **kwargs):
        startTime = time.time() * 1000
        result = method(*args, **kwargs)
        endTime = time.time() * 1000

        print(endTime - startTime, 'ms')
        return result

    return wrapper

def timemeavg(method):
    def wrapper(*args, **kwargs):
        startTime = time.time() * 1000
        result = method(*args, **kwargs)
        endTime = time.time() * 1000

        time_took = endTime - startTime
        #print(endTime - startTime, 'ms')
        if result:
            return result, time_took
        else:
            return time_took

    return wrapper

def extreme(num):
    return abs(1e-15 - float(num))

def get_dict_attr(obj,attr):
    """http://stackoverflow.com/questions/3681272/can-i-get-a-reference-to-a-python-property"""
    for obj in [obj]+obj.__class__.mro():
        if attr in obj.__dict__:
            return obj.__dict__[attr]

@timemeavg
def benchmark():
    x = 0
    while x < 1e6:
        x += 1

def make_iter(obj):
    if isinstance(obj, collections.Iterable):
        return obj
    else:
        return [obj]


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    """http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks"""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def math(obj, func):
    print(type(sup.__thisclass__()))

class Math():
    """Add mathematical methods to any class"""
    def __init__(self, func, methods=('add', 'sub', 'mul', 'truediv')):
        self._func = func
        self._methods = methods

    def __call__(self, obj):
        self._obj = obj

        #add = obj.__add__
        #obj.__add__ = alter(add)

        for method_name in self._methods:
            method = eval('obj.__{}__'.format(method_name))
            method = self.alter(method)
            exec('obj.__{}__ = method'.format(method_name))

        return obj

    def alter(self, op):
        return lambda s, o: self._obj(self._func(op, s, o))

@Math(lambda op, s, other: op(s, other*4), methods=('add', 'sub'))
class Test(int):
    pass



def synfunc(list):
    def funcwrapper(func):
        list.append(func)
        del func
    return funcwrapper

def name2conts(func):
    def wrapper(fname):
        with open(fname, 'r') as file:
            return func(file.read())
    return wrapper
