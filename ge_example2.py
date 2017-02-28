from fractions import Fraction
from getools import print_matrix


m = [[Fraction(1, 1), Fraction(2, 1), Fraction(3, 1), Fraction(0, 1)],
     [Fraction(3, 1), Fraction(4, 1), Fraction(7, 1), Fraction(2, 1)],
     [Fraction(6, 1), Fraction(5, 1), Fraction(9, 1), Fraction(11, 1)]]


print_matrix(m)

# -3R1 + R2, -6R1 + R3
for i in range(len(m[0])):
    m[1][i] += -3 * m[0][i]
    m[2][i] += -6 * m[0][i]

print_matrix(m)

# (-1/2)R2
for i in range(len(m[1])):
    m[1][i] *= Fraction(-1, 2)

print_matrix(m)

# 7R2 + R3
for i in range(len(m[1])):
    m[2][i] += 7 * m[1][i]

print_matrix(m)
