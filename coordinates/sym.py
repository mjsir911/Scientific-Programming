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
    func.__globals__['math'] = sympy # amazing that i can do this
    @functools.wraps(func)
    def wrapper(coord):
        coord = list(coord)
        for i, dim in enumerate(coord):
            elif isinstance(dim, int):
                coord[i] = sympy.Number(dim)
            else:
                coord[i] = sympy.sympify(dim)
        return func(coord)
    return wrapper
