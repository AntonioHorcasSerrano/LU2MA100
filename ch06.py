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
# print(vecteurpropre)
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

def solve(L,U,b):
    """ array x array x vector --> vector
        Hypothèse: L et U carrées de taille n et b vecteur de R^n
        Retourne la solution du système linéaire comme vector R^n
    """
    n = L.shape[0]
    y = np.zeros(n, dtype = float)
    x = np.zeros(n, dtype = float)
    # fait Ly = b
    # y[0]=b[0]
    # y[1]=b[1]-L[1][0]*y[0]
    # y[2]=b[2]-(L[2][0]*y[0]+L[2][1]*y[1])
    for i in range(n):
        somme = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b[i] - somme
    print("y:",y)
    # y = np.linalg.solve(L,b)
    # fait Ux = y
    for i in reversed(range(n)):
        somme = sum(U[i][j] * x[j] for j in range(i+1, n))
        x[i] = (y[i] - somme) / U[i][i]
        print("somme: %d " % somme)
        # x = np.linalg.solve(U,y)
    print(x)
    return x

A = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
L = np.array([[ 1.        ,  0.        ,  0.        ],[-0.5       ,  1.        ,  0.        ],[ 0.        , -0.66666667,  1.        ]])
U = np.array([[ 2.        , -1.        ,  0.        ],[ 0.        ,  1.5       , -1.        ],[ 0.        ,  0.        ,  1.33333333]])
b = np.array([2,1,1])
solve(L,U,b)
print(np.linalg.det(L) * np.linalg.det(U))
print(np.linalg.det(A))
