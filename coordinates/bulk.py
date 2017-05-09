#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import convert


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

def str2coord(coord_string):
    """
      >>> str2coord('(1, 2)')
      ('1', '2')
    """
    assert coord_string[0] + coord_string[-1] == '()'
    coord = coord_string.strip('()').split(',')
    coord = tuple(z.strip() for z in coord)

    return coord

def read_and_process(func):
    def wrapper(read_fp, write_fp):
        for line in read_fp:
            write_fp.write(str(func(str2coord(line))))
    return wrapper

convert_cartesian_points = read_and_process(convert.cart2pol)
convert_polar_points     = read_and_process(convert.pol2cart)

import io
outF = io.StringIO('(1, 2)')
inF  = io.StringIO()
convert_cartesian_points(outF, inF)




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
