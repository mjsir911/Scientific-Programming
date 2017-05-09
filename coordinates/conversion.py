#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from sym import symcoords

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

@symcoords
def cart2pol(cartesian_coordinate):
    """
      >>> cart2pol((3, 4))
      (5, atan(3/4))
      >>> cart2pol((-3, 2))
      (sqrt(13), -atan(3/2))
    """
    x, y = cartesian_coordinate
    r = math.sqrt(pow(x, 2) + pow(y, 2))
    t = math.atan(x / y)
    return r, t

@symcoords
def pol2cart(polar_coordinate):
    """
      >>> pol2cart((3, 'pi'))
      (-3, 0)
      >>> pol2cart((-10, 'pi/6'))
      (-5*sqrt(3), -5)

    """
    r, t = polar_coordinate
    x = r * math.cos(t)
    y = r * math.sin(t)
    return x, y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
