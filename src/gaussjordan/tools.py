#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from fractions import Fraction
from .. import geometry
from ..matrices import dat2list

__appname__     = ""
__author__      = "Jeffrey Elkner"
__copyright__   = ""
__credits__     = ["Jeffrey Elkner", "Marco Sirabella", "Ali Abbas"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

def print_matrix(m):
    for row in m:
        print('|{0:6s}{1:6s}{2:6s}| {3:6s}|'.format(*[str(val) for val in row]))
    print()


class Reduced_Echelon(geometry.Matrix):
    """
    Transform matrix m into reduced row echelon form
      >>> matrix = Reduced_Echelon(
      ...         geometry.Vector(1, -2, 3, 9),
      ...         geometry.Vector(-1, 3, 0, -4),
      ...         geometry.Vector(2, -5, 5, 17),
      ...         )

      >>> print(matrix)
    """
    def __init__(self, *args):
        super().__init__(*args)

        for row in range(len(self)):
            self.one(row)

    def one(self, row):
        a = row
        b = (row + 1) % 3
        c = (row + 2) % 3
        # Multiply the row <row> by the multiplicative inverse of the <row>th element
        self.div(a,    self[a, a])
        #Zero the other two rows on column <row>
        self.sub(b, a, self[b, a])
        self.sub(c, a, self[c, a])


    def mul(self, Ri, k):
        """
        deprecated
        """
        self[Ri] *= k

    def div(self, Ri, k):
        self[Ri] *= 1 / k
        #something something fractions
        #self[Ri] *= F = Fraction(1, m[0][0])

    def add(self, Ri, Rj, k):
        """
        deprecated
        """
        self[Ri] += k * self[Rj]


    def sub(self, Ri, Rj, k):
        #self.mul(Rj, k)
        #self[Ri] += self[Rj]
        #self.mul(Rj, 1/k)
        self[Ri] -= k * self[Rj]
