from sympy import *
from sympy.abc import rho, phi

x=Symbol("x",real=True)
X = Matrix([rho*cos(phi), rho*sin(phi), rho**2])
print(X.shape[0])
Y = Matrix([rho, phi])

print(X.jacobian(Y))

from scipy import misc

def f(x):
    return (1.0/4.0)*x**3+(3.0/4.0)*x**2-(3.0/2.0)*x-2

def newton1d(f, point, epsilon=1e-6):
    while True:
        nextpoint = point - f(point) / diff(f(x),x).subs(x,point)
        dif = abs(nextpoint - point)
        if dif < epsilon:
            break
        point = nextpoint
    return point

point = 4
x0 = newton1d(f, point)

print('x: ', point)
print('x0: ', x0)
print("f(x0) = ", ((1.0/4.0)*x0**3+(3.0/4.0)*x0**2-(3.0/2.0)*x0-2 ))