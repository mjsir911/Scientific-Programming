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
