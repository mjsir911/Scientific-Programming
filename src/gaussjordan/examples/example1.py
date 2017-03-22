from .. import tools
from fractions import Fraction

m = [[1, -2, 3, 9], [-1, 3, 0, -4], [2, -5, 5, 17]]
tools.print_matrix(m)
tools.Reduced_Echelon.mul(m, 2, Fraction(1, 2))
tools.print_matrix(m)
add_row(m, 1, 1, 2)
add_row(m, -1, 1, 3)
tools.print_matrix(m)
add_row(m, Fraction(1, 2), 2, 3)
tools.print_matrix(m)
add_row(m, -3, 3, 2)
add_row(m, -3, 3, 1)
tools.print_matrix(m)
add_row(m, 2, 2, 1)
tools.print_matrix(m)
