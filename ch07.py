from sympy import *
from sympy.abc import rho, phi

x=Symbol("x",real=True)
X = Matrix([rho*cos(phi), rho*sin(phi), rho**2])
print(X.shape[0])
Y = Matrix([rho, phi])

print(X.jacobian(Y))

from scipy import misc

# def f(x):
#     return (1.0/4.0)*x**3+(3.0/4.0)*x**2-(3.0/2.0)*x-2

def newton(F, DF, x0, eps=1e-10, N=1000):
    while N > 0 and abs(F(x0)) >= eps:
        x1 = x0 - F(x0) / DF(x0)
        x0 = x1
    return x0

import math
F = lambda x: math.exp(-x)-x
DF = lambda x: -1-(math.exp(-x))
def newton(F,DF,x0,eps=1e-10,N=10):
    xn = x0
    for _ in range(0,N+1):
        if abs(F(xn)) < eps:
            return xn
        xn = xn - F(xn)/DF(xn)
    return None

print(newton(F,DF,1))

import numpy as numpy
