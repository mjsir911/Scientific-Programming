from .. import tools
from fractions import Fraction


m = [[Fraction(2, 1), Fraction(1, 1), Fraction(-1, 1), Fraction(8, 1)],
     [Fraction(-3, 1), Fraction(-1, 1), Fraction(2, 1), Fraction(-11, 1)],
     [Fraction(-2, 1), Fraction(1, 1), Fraction(2, 1), Fraction(-3, 1)]]

reduced_row_echelon(m)
print_matrix(m)
