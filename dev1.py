import numpy as np
import matplotlib.pyplot as plt
from sympy import *
init_printing()

k=Symbol("k",integer=True,positive=True)
e = Symbol(r"\varepsilon", real=True, positive=True) # définit epsilon positif

e=0.1
def truncated_qa(n):
    return Sum((-1)**k/(2*k+1), (k, 0, n)).doit().evalf()

def tr_qa_increase(e):
    n=1
    while (Abs((pi-4*truncated_qa(n)))).evalf() >= e:
        n=n+1
    return n

print(tr_qa_increase(0.05))

l = [(n,(Abs((pi-4*truncated_qa(n)))).evalf()) for n in range(3,101)]
plt.scatter(*zip(*l))
plt.title(r'$\left|\pi -4 S_n\right|$ en fonction de $n$')
plt.xlabel(r'$n$')
plt.ylabel(r'$\left|\pi -4 S_n\right|$')
plt.show()