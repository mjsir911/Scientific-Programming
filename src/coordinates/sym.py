#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sympy
import functools

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


def symcoords(func):
    func.__globals__['math'] = sympy  # amazing that i can do this

    @functools.wraps(func)
    def wrapper(coord):
        coord = tuple(sympy.sympify(str(c)) for c in coord)
        return func(coord)
    return wrapper


def general(func):
    func.__globals__['math'] = sympy

    @functools.wraps(func)
    def wrapper(*args):
        args = tuple(sympy.sympify(str(a).replace("'", '')) for a in args)
        # args = tuple(sympy.sympify(str(a) for a in args))
        return func(*args)
    return wrapper
