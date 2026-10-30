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
# [[0,0],[3,3],[7,0],[3,1],[5,2],[4,5],[1,4],[9,6]]
# les point seront échangés si la fonction gauche renvoi False
assert gauche([0,0],[3,3],[7,0]) == True
assert gauche([0,0],[3,3],[3,1]) == True
assert gauche([0,0],[3,3],[5,2]) == True
assert gauche([0,0],[3,3],[4,5]) == False
assert gauche([0,0],[4,5],[1,4]) == False
assert gauche([0,0],[1,4],[9,6]) == True
# [1,4]
assert gauche([1,4],[0,0],[3,3]) == False
assert gauche([1,4],[3,3],[7,0]) == True
assert gauche([1,4],[3,3],[3,1]) == True
assert gauche([1,4],[3,3],[5,2]) == True
assert gauche([1,4],[3,3],[4,5]) == False
assert gauche([1,4],[4,5],[9,6]) == True
# [4,5]
assert gauche([4,5],[0,0],[3,3]) == False
assert gauche([4,5],[3,3],[7,0]) == False
assert gauche([4,5],[7,0],[3,1]) == True
assert gauche([4,5],[7,0],[5,2]) == True
assert gauche([4,5],[7,0],[1,4]) == True
assert gauche([4,5],[7,0],[9,6]) == False
# [9,6]
assert gauche([9,6],[0,0],[3,3]) == True
assert gauche([9,6],[0,0],[7,0]) == False
assert gauche([9,6],[7,0],[3,1]) == True
assert gauche([9,6],[7,0],[5,2]) == True
assert gauche([9,6],[7,0],[4,5]) == True
assert gauche([9,6],[7,0],[1,4]) == True
# [7,0]
assert gauche([7,0],[0,0],[3,3]) == True
assert gauche([7,0],[0,0],[3,1]) == True
assert gauche([7,0],[0,0],[5,2]) == True
assert gauche([7,0],[0,0],[4,5]) == True
assert gauche([7,0],[0,0],[1,4]) == True
assert gauche([7,0],[0,0],[9,6]) == True
# [0,0]

def prochain_point(E,X):
    x = E.index(X)
    y1 = (x + 1) % len(E)
    for y2 in range(len(E)):
        if x == y2 or y1 == y2:
            continue
        print(E[x],E[y1],E[y2],gauche(E[x], E[y1], E[y2]))
        if gauche(E[x], E[y1], E[y2]) == False:
            y1 = y2
    return E[y1]
        
print(prochain_point([[0,0],[3,3],[7,0],[3,1],[5,2],[4,5],[1,4],[9,6]],[0,0]))