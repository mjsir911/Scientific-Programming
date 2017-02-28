def print_matrix(m):
    for row in m:
        vals = [str(val) for val in row]
        print('|{0:18s}{1:18s}{2:18s}| {3:18s}|'.format(*vals))
    print()
