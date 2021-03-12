import numpy as np
import sympy as sp
import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

def puissance(A, x0, k):
    vecteur = np.random.random_sample((2,))
    for i in range(k):
        nv = np.dot(A, vecteur)
        vecteur = nv / np.linalg.norm(nv)
        print(vecteur)
    return vecteur

vecteurpropre = np.array(puissance(np.array([[0.5, 0.5], [0.2, 0.8]]), np.random.random_sample((2,)), 10))
print(vecteurpropre)
valpropre = np.dot(np.dot(np.array([[0.5, 0.5], [0.2, 0.8]]),vecteurpropre), vecteurpropre)

print(valpropre)
print(sp.Matrix([[1, 1], [1e-100, 1]]).is_diagonalizable())

https://www.quantstart.com/articles/LU-Decomposition-in-Python-and-NumPy/

A = scipy.array([ [7, 3, -1, 2], [3, 8, 1, -4], [-1, 1, 4, -1], [2, -4, -1, 6] ])
P, L, U = scipy.linalg.lu(A)

print ("A:")
pprint.pprint(A)

print ("P:")
pprint.pprint(P)

print ("L:")
pprint.pprint(L)

print ("U:")
pprint.pprint(U)