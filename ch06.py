import numpy as np
import sympy as sp
import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

def puissance(A, x0, k):
    vecteur = np.random.random_sample((2,))
    for _ in range(k):
        nv = np.dot(A, vecteur)
        vecteur = nv / np.linalg.norm(nv)
        # print(vecteur)
    return vecteur

vecteurpropre = np.array(puissance(np.array([[0.5, 0.5], [0.2, 0.8]]), np.random.random_sample((2,)), 10))
print(vecteurpropre)
valpropre = np.dot(np.dot(np.array([[0.5, 0.5], [0.2, 0.8]]),vecteurpropre), vecteurpropre)

# print(valpropre)
# print(sp.Matrix([[1, 1], [0, 1]]).is_diagonalizable())

# https://www.quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy/

# A = scipy.array([ [7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
# P, L, U = scipy.linalg.lu(A)

# print ("A:")
# pprint.pprint(A)

# print ("P:")
# pprint.pprint(P)

# print ("L:")
# pprint.pprint(L)

# print ("U:")
# pprint.pprint(U)


# https://www.youtube.com/watch?v=BFYFkn-eOQk

def LU(A):
    if not sp.Matrix(A).is_diagonalizable(): return None
    n = A.shape[0]
    L = np.identity(n, dtype = float)
    U = np.zeros((n,n), dtype = float)
    for j in range(n):
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A[i][j] - s1
        for i in range(j, n):
                s2 = sum(U[k][j] * L[i][k] for k in range(j))
                L[i][j] = (A[i][j] - s2) / U[j][j]
    return L,U

A = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
print(LU(A))