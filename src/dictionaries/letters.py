#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string

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

def count(sentence):
    """
      >>> count('marco') == {'m': 1, 'a': 1, 'r': 1, 'c': 1, 'o': 1}
      True
      >>> count('banana') == {'b': 1, 'a': 3, 'n': 2}
      True
      >>> count('Mississippi') == {'m': 1, 'i': 4, 's': 4, 'p': 2}
      True
      >>> count('Jeff') == {'j': 1, 'e': 1, 'f': 2}
      True
      >>> len(count('Hello World!'))
      7
    """
    counts = {}
    for letter in sentence:
        if letter in string.ascii_lowercase:
            pass
        elif letter in string.ascii_uppercase:
            letter = letter.lower()
        else:
            continue

        counts[letter] = counts.get(letter, 0) + 1
    return counts

def main():
    s = count(input('Please input a string: '))
    for L in sorted(s):
        print('{}  {}'.format(L, s[L]))


if __name__ == '__main__':
    main()
