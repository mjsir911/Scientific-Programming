from fractions import Fraction

def print_matrix(m):
    for row in m:
        print('|{0:6s}{1:6s}{2:6s}| {3:6s}|'.format(*[str(val) for val in row]))
    print()


def mul_row(m, k, ri):
    for i in range(len(m[ri-1])):
        m[ri-1][i] *= k 


def add_row(m, k, ri, rj):
    for i in range(len(m[ri-1])):
        m[rj-1][i] += k * m[ri-1][i]


def reduced_row_echelon(m):
    """Transform matrix m into reduced row echelon form"""
    # Multiply the first row by the multiplicative inverse of the first element
    recip = Fraction(1, m[0][0])
    for i in range(len(m[0])):
        m[0][i] *= recip
