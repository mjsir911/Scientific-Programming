from fractions import Fraction
from getools import print_matrix


m = [[Fraction(2, 1), Fraction(1, 1), Fraction(-1, 1), Fraction(8, 1)],
     [Fraction(-3, 1), Fraction(-1, 1), Fraction(2, 1), Fraction(-11, 1)],
     [Fraction(-2, 1), Fraction(1, 1), Fraction(2, 1), Fraction(-3, 1)]]

print_matrix(m)

# (1/2)R1
for i in range(len(m[0])):
    m[0][i] *= Fraction(1, 2)

print_matrix(m)

# 3R1 + R2, 2R1 + R3
for i in range(len(m[0])):
    m[1][i] += 3 * m[0][i]
    m[2][i] += 2 * m[0][i]

print_matrix(m)

# 2R2
for i in range(len(m[1])):
    m[1][i] *= 2

print_matrix(m)

# -2R2 + R3
for i in range(len(m[1])):
    m[2][i] += -2 * m[1][i]

print_matrix(m)

# -R2
for i in range(len(m[1])):
    m[2][i] *= -1

print_matrix(m)

# -R3 + R2, (1/2)R3 + R1
for i in range(len(m[1])):
    m[1][i] += -1 * m[2][i]
    m[0][i] += Fraction(1, 2) * m[2][i]

print_matrix(m)

# (-1/2)R2 + R1
for i in range(len(m[1])):
    m[0][i] += Fraction(-1, 2) * m[1][i]

print_matrix(m)
