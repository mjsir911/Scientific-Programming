from sympy import symbols, simplify
from gjgentools import print_matrix

a, b, c, d, e, f, g, h, i, j, k, m = symbols('a b c d e f g h i j k m')

m = [[a, b, c, d],
     [e, f, g, h],
     [i, j, k, m]]

print_matrix(m)

# (1/a)R1
val = m[0][0]
for i in range(len(m[0])):
    m[0][i] *= (1 / val)

print_matrix(m)

# (-1/e)R1 + R2, (-1/i)R1 + R3
val1 = m[1][0]
val2 = m[2][0]
for i in range(len(m[0])):
    m[1][i] += -val1 * m[0][i]
    m[2][i] += -val2 * m[0][i]

print_matrix(m)

# Make leading coefficient of row2 1
val = m[1][1]
for i in range(len(m[1])):
    m[1][i] *= (1 / val)

print_matrix(m)

# Add the negative of the leading coeff of R3 times R2 to R3
val = -m[2][1]
for i in range(len(m[1])):
    m[2][i] += val * m[1][i]

print_matrix(m)

# Make leading coefficient of row3 1
val = m[2][2]
for i in range(len(m[2])):
    m[2][i] *= (1 / val)

print_matrix(m)

# Use R3 to make the 3rd elements in R1 and R2 0 
val1 = -m[1][2]
val2 = -m[0][2]
for i in range(len(m[1])):
    m[1][i] += val1 * m[2][i]
    m[0][i] += val2 * m[2][i]

print_matrix(m)

# Use R2 to make the 2nd element in R1 0 
val = -m[0][1]
for i in range(len(m[0])):
    m[0][i] += val * m[1][i]

print_matrix(m)

# Now pretty print the results:
print("val1 =", simplify(m[0][3]))
print("val2 =", simplify(m[1][3]))
print("val3 =", simplify(m[2][3]))
