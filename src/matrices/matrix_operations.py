import numpy as np

A = np.matrix( ((12, -10), (-7, 0), (4, -3)) )
B = np.matrix( ((-7, -4), (5, 2), (3, -1)) )
C = np.matrix( ((1, 3, 4), (8, 6, -5), (-2, -1, 7)) )
D = np.matrix( ((-8, 5, -6), (7, -4, 2), (-3, 10, -10)) )

print("A + B = \n{0}".format(A + B))
print("-B = \n{0}".format(-B))
print("3C = \n{0}".format(3 * C))
print("CD = \n{0}".format(C * D))
print("CB = \n{0}".format(C * B))
print("D^T = \n{0}".format(np.transpose(D)))
print("DB = \n{0}".format(D * B))
print("A^TB = \n{0}".format(np.transpose(A) * B))
