#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Webassign practice problems:
  >>> series(64, (2, 6))
  (..., (16.0, 48.0), (8.0, 8.0))
  >>> series(65, (6, 3, 4))
  (..., (30.0, 15.0, 20.0), (5.0, 5.0, 5.0))
  >>> parallel(180, (6, 5, 12))
  (..., (180.0, 180.0, 180.0), (30.0, 36.0, 15.0))

  >>> r1, r2, r3 = 2, 30, 20
  >>> parallel(float('nan'), (r2, r3))[0]
  12.0
  >>> series(float('nan'), (_, r1))[0]
  14.0

"""

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

rs = [12.5, 14.7, 19.2]
i_v = 60

def current(V_s, r_s):
    return tuple(V / r for V, r in zip(V_s, r_s))

"""
def parallel(voltage, resistances):
    total_resistance = 1 / sum(1 / resistance for resistance in resistances)
    voltages = [float(voltage)] * len(resistances)
    del voltage
    currents = [voltage / resistance for voltage, resistance in zip(voltages, resistances)]
    return total_resistance, voltages, currents
"""

import fractions
def parallel(V, r_s):
    """

      >>> r1, r2, r3 = 2, 30, 20
      >>> parallel(float('nan'), (r2, r3))[0]
      12.0

    """

    sig_r = float(1 / sum(fractions.Fraction(1, r) for r in r_s))
    V_s = (float(V),) * len(r_s)
    del V
    A = current(V_s, r_s)
    return sig_r, V_s, A

def series(V, r_s):
    sig_r = sum(r_s)
    V_s = tuple(r * V / sig_r for r in r_s)
    A = current(V_s, r_s)
    return sig_r, V_s, A

#print(series(65, [6, 3, 4]))
#print(series([12.5, 14.7, 19.1], 60))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)
