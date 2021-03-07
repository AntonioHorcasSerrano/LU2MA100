# http://razik.univ-tln.fr/cn/capes_2017_pb2.html

import numpy as np

def premier_point(E):
    min = E[0]
    index = 0
    for i, point in enumerate(E[1:], 1):
        if point[0] < min[0]:
            min = point
            index = i
    return index

assert premier_point([[2, 0], [-1, 1], [3, 0]]) == 1

def gauche(X, Y1 ,Y2):
    det = np.linalg.det(np.array([[Y1[0] - X[0], Y1[1] - X[1]],  [Y2[0] - X[0], Y2[1] - X[1]]]))
    if det != 0:
        return False if det > 0 else True
    else:
        return False if X==Y2 else True        

assert gauche([0, 0], [-1, 2], [0, 0]) == False
assert gauche([0, 0], [0, 0], [-1, 2]) == True
assert gauche([0, 0], [-1, 2], [-2, 2]) == False
assert gauche([0, 0], [-2, 2], [-1, 2]) == True