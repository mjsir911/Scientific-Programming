from gjtools import print_matrix, mul_row, add_row
from fractions import Fraction

m = [[1, -2, 3, 9], [-1, 3, 0, -4], [2, -5, 5, 17]]
print_matrix(m)
mul_row(m, Fraction(1, 2), 3)
print_matrix(m)
add_row(m, 1, 1, 2)
add_row(m, -1, 1, 3)
print_matrix(m)
add_row(m, Fraction(1, 2), 2, 3)
print_matrix(m)
add_row(m, -3, 3, 2)
add_row(m, -3, 3, 1)
print_matrix(m)
add_row(m, 2, 2, 1)
print_matrix(m)
