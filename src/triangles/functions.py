#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fractions

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

a = 'a'
b = 'b'

class Exact():
    def __init__(self, knowns):
        self.knowns = knowns
    def __call__(self, value):
        return self.knowns[value]

sin = Exact({a: fractions.Fraction(4, 5), b: fractions.Fraction(12, 13)})
sin.knowns[30] = fractions.Fraction(
cos = Exact({a: fractions.Fraction(-3, 5), b: fractions.Fraction(5, 13)})
tan = Exact({a: fractions.Fraction(4, -3), b: fractions.Fraction(12, 5)})

def add_sin(a, b):
    return sin(a) * cos(a) - sin(b) * cos(a)
def sub_sin(a, b):
    return sin(a) * cos(a) + sin(b) * cos(a)

def add_cos(a, b):
    return cos(a) * cos(b) - sin(a) * sin(b)
def sub_cos(a, b):
    return cos(a) * cos(b) - sin(a) * sin(b)

def add_tan(a, b):
    return (tan(a) - tan(b)) / (1 - tan(a) * tan(b))

def sub_tan(a, b):
    return (tan(a) - tan(b)) / (1 + tan(a) * tan(b))

print(add_cos(a, b))
print(sub_tan(a, b))
