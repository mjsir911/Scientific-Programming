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

def madlib(filep):
    msg = filep.read()[:-1]
    parts = []
    i = 0
    while True:
        part = msg[slice(msg.find('['), msg.find(']') + 1)]
        spart = part[1: -1]
        if part == '':
            break
        elif spart.isnumeric():
            msg = msg.replace(part, '{{{}}}'.format(int(spart)), 1)
        else:
            parts.append(spart)
            msg = msg.replace(part, '{{{}}}'.format(i), 1)
            i += 1

    imsg = 'Please enter a {}: '
    msg  = msg.format(*[input(imsg.format(part)) for part in parts])
    print()
    return msg


with open('madlib.txt', 'r') as file:
    print(madlib(file))
