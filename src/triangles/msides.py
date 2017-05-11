#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import functools
import operator

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

def triangle(func):
    @functools.wraps(func)
    def wrapper(A=None, B=None, C=None, a=None, b=None, c=None):
        t = {
                'a': {'side': a, 'angle': A},
                'b': {'side': b, 'angle': B},
                'c': {'side': c, 'angle': C}
                }
        return func(t)
    return wrapper

sin = lambda d: math.sin(math.radians(d))

@triangle
def law_of_sin(t):
    los = []
    for v in t.values():
        if v['side'] is not None and v['angle'] is not None:
            los.append(sin(v['angle']) / v['side'])
    assert sum(los) / len(los) == los[0]
    return los[0]

@triangle
def law_of_cos(t):
    pass

#print(law_of_sin(A=35, a=12, b=16))
@triangle
def ASA(t):
    los = sin(A) / a
    B = math.degrees(math.asin(b * los))
    assert los == sin(B) / b
    C = 180 - A - B
    return A, B, C, a, b, c

#print(ASA(A=35, a=12, b=16))

def area(A=None, B=None, C=None, a=None, b=None, c=None):
    return (b * c * sin(A)) / 2

def ssa(A=None, B=None, C=None, a=None, b=None, c=None):
    pass

def hi(side, t):
    otwo = tuple(i for i in t.keys() if i is not side)
    a = t[side]['side'] ** 2 - sum(t[i]['side'] ** 2 for i in otwo)
    b = -2 * functools.reduce(operator.mul, [t[i]['side'] for i in otwo])
    return math.degrees(math.acos(a / b))

@triangle
def sss(t):
    a, b, c = (t[i]['side'] for i in ('a', 'b', 'c'))
    A = hi('a', t)
    B = hi('b', t)
    C = hi('c', t)
    return A, B, C

print(sss(a=8, b=10, c=5))
#print(area(b=8, c=12, A=135))
