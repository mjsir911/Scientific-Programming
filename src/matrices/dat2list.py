#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

def from_memory(filename):
    with open(filename, 'r') as file:
        contents = file.read()
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


print(from_memory('matrices.dat'))

def from_memory(filename):
    with open(filename, 'r') as file:
        content = file.read()
    matrices = content.split("##")
    matrices = [item.strip() for item in matrices]
    matrices = [item.split("\n") for item in matrices]
    matrices = [[row.split(';') for row in matrix] for matrix in matrices]
    matrices = [[[int(item) for item in row] for row in matrix] for matrix in matrices]

    return matrices


print(from_memory('matrices.dat'))
