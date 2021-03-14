import numpy as np
import sympy as sp
import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

diff =0

def puissance1(A, x0, k):
    w = np.dot(A, x0)
    norm_w = np.linalg.norm(w)
    for _ in range(k):
        nv = np.dot(A, x0)
        norm_nv = np.linalg.norm(nv)
        if (abs(norm_w - norm_nv) < 1E-5):
            break
        norm_w = norm_nv
        x0 = nv / np.linalg.norm(nv)
    return x0



print(puissance1(np.array([[0, 6, -1], [6, 0, 6],[-1, 6, 0]]), np.random.random_sample((3,)), 200))
print(np.linalg.eig(np.array([[0, 6, -1], [6, 0, 6],[-1, 6, 0]])))