from sympy import symbols

def print_matrix(m):
    for row in m:
        print(row)
    print()

a, b, c, d, e, f, g, h, j, k, m, n = symbols('a b c d e f g h j k m n')
m = [[a, b, c, d], [e, f, g, h], [j, k, m, n]]

# (1/a11)R1, (1/a21)R2, (1/a31)R3
for row in m:
    n = row[0]
    for i, val in enumerate(row):
        row[i] *= (1 / n)

print_matrix(m)

# -R2 + R3, -R1 + R2
for i in range(len(m[0])):
    m[2][i] -= m[1][i]
    m[1][i] -= m[0][i]

print_matrix(m)

# (1/a22)R2, (1/a32)R3
for row in m[1:]:
    n = row[1]
    for i, val in enumerate(row[1:]):
        row[i] *= (1 / n)

print_matrix(m)

# -R2 + R3
for i in range(len(m[0])):
    m[2][i] -= m[1][i]

print_matrix(m)

# (1/a33)R3
n = m[2][2]
m[2][2] *= (1 / n)
m[2][3] *= (1 / n)

print_matrix(m)
