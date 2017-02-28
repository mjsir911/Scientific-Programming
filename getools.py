def print_matrix(m):
    for row in m:
        print('|{0:6s}{1:6s}{2:6s}| {3:6s}|'.format(*[str(val) for val in row]))
    print()
