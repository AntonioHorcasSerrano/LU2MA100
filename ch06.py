import numpy as np
import sympy as sp

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