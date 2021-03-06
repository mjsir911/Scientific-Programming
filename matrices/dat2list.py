#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from ..misc import synfunc, name2conts

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

from_memories = []

@synfunc(from_memories)
@name2conts
def from_memory(contents):
    """
      >>> import os
      >>> filename = os.path.dirname(__file__) + '/matrices.dat'
    """

    matrices = contents.split('##')
    for i, matrix in enumerate(matrices):
        rows = matrix.strip().split('\n')
        for j, row in enumerate(rows):
            columns = row.split(';')
            for k, column in enumerate(columns):
                columns[k] = int(column)
            rows[j] = columns
        matrices[i] = rows
    return matrices

@synfunc(from_memories)
@name2conts
def from_memory(contents):
    matrices = content.split("##")
    matrices = [item.strip() for item in matrices]
    matrices = [item.split("\n") for item in matrices]
    matrices = [[row.split(';') for row in matrix] for matrix in matrices]
    matrices = [[[int(item) for item in row] for row in matrix] for matrix in matrices]

    return matrices

from_memory = from_memories[0]
