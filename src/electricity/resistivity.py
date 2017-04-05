#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import scipy.constants

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

def resistance(p, length, gauge):
    L = length
    A = (1 / gauge) * scipy.constants.inch * 100
    return (p * L) / A
