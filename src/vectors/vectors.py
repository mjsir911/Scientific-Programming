#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import collections
import test
from numbers import Number

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

def add_vectors(u, v):
    """
      >>> add_vectors([1, 0], [1, 1])
      [2, 1]
      >>> add_vectors([1, 2], [1, 4])
      [2, 6]
      >>> add_vectors([1, 2, 1], [1, 4, 3])
      [2, 6, 4]
      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
      [13, -4, 13, 5]
      >>> a = [1, 2, 3]
      >>> b = [1, 1, 1]
      >>> add_vectors(a, b)
      [2, 3, 4]
      >>> a
      [1, 2, 3]
      >>> b
      [1, 1, 1]
    """
    return list(Vector(u) + Vector(v))

def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
      >>> a = [1, 2, 3]
      >>> scalar_mult(4, a)
      [4, 8, 12]
      >>> a
      [1, 2, 3]
    """
    return list(s * Vector(v))


def math(cls, sup, func):
    def add(self, value):
        #return cls(sup.__add__(self, value))
        #print('{} {} {}'.format(self, func, value))
        return cls(func(sup.__add__, self, value))
    cls.__add__ = add
    cls.__radd__ = lambda s, v: cls(sup.__radd__(s, v))

class Vector(tuple):
    """Vector"""


    #Init

    def __new__(cls, *items):
        if len(items) == 1 and isinstance(items[0], collections.Iterable):
            items = items[0]
        self = super().__new__(cls, items)
        #x = lambda f, s, v: [f(v) for s, v in zip(s, v)]
        #math(cls, super(), x)
        return self

    def __init__(self, *items):
        assert all(isinstance(x, Number) for x in self), [type(x) for x in self]
        self._dimension = len(self)


    #Formatting

    def __repr__(self):
        return "Vector" + super().__repr__()


    #Iterability

    def __getitem__(self, index):
        if isinstance(index, slice):
            pass
        return super().__getitem__(index)


    """Math"""

    def __add__(self, value):
        assert self._dimension == value._dimension
        return Vector(a + b for a, b in zip(self, value))
    def __radd__(self, value):
        return self + value

    def __sub__(self, value):
        assert self._dimension == value._dimension
        return Vector(a - b for a, b in zip(self, value))

    def __mul__(self, value):
        return Vector(a * value for a in self)
    def __rmul__(self, value):
        return self * value

    def __truediv__(self, value):
        return Vector(a / value for a in self)
    def __rtruediv__(self, value):
        return self / value

    def __neg__(self):
        return Vector(-a for a in self)

    """Comparators"""
    def __gt__(self, other):
        truey = []
        for my_coord, other_coord in zip(self, other):
            truey.append(my_coord > other_coord)
        return all(truey)

    def __lt__(self, other):
        truey = []
        for my_coord, other_coord in zip(self, other):
            truey.append(my_coord < other_coord)
        return all(truey)





class Matrix(list):
    """

    >>> z = Matrix(
    ...    Vector(1, 2, 3),
    ...    Vector(4, 5, 6),
    ...    Vector(7, 8, 9),
    ... )

    >>> print(z)
    Matrix((1, 2, 3), (4, 5, 6), (7, 8, 9))

    """

    def __init__(self, *vectors):
        if len(vectors) == 1 and isinstance(vectors[0], collections.Iterable):
            vectors = vectors[0]
        super().__init__(vectors)
        assert all(isinstance(x, Vector) for x in self)
        self._dimension = len(self)

    def __repr__(self):
        return "Matrix" + str(tuple(tuple(v) for v in self))

    def __setitem__(self, index, value):
        super().__setitem__(index, value)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            obj = self
            for i in index:
                obj = obj[i]
            return obj
        return super().__getitem__(index)
    def __getitem__(self, index):
        if isinstance(index, tuple):
            obj = self
            for i in index:
                obj = obj[i]
            return obj
        return super().__getitem__(index)

Void = None

class Space(dict):
    """
    >>> time = Space()
    >>> type(time)
    <class '....Space'>
    >>> time[1, 2]
    >>> time[10000, 54321] = "Spaaaaaaaaaace"
    >>> print(time[10000, 54321])
    Spaaaaaaaaaace
    """

    def __init__(self, dimensions):
        self.dimensions = dimensions
        super().__init__()

    def confcoord(func):
        def wrapper(self, coordinate, *args, **kwargs):
            assert isinstance(coordinate, collections.Iterable)
            assert len(coordinate) == self.dimensions, coordinate
            return func(self, coordinate, *args, **kwargs)
        return wrapper

    @confcoord
    def __getitem__(self, coordinate):
        return super().get(coordinate, Void)

    @confcoord
    def __setitem__(self, coord, value):
        super().__setitem__(coord, value)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
