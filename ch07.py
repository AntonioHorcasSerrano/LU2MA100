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

def F(x):
    return x**3 - 27

def DF(x):
    return 3*x**2

# newton(F, DF, 1)

def racine1(x, n):
    F = y**n - x
    DF = diff(F,y)
    print(DF)
    #newton(F, DF, 1)