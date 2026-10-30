import numpy as np
import matplotlib.pyplot as plt
from sympy import *
init_printing()

k=Symbol("k",integer=True,positive=True)
e = Symbol(r"\varepsilon", real=True, positive=True) # définit epsilon positif

e=0.1
def truncated_qa(n):
    return Sum((-1)**k/(2*k+1), (k, 0, n)).doit().evalf()

def truncated_qa1(n):
    s=0
    for k in range(0,n+1):
        s=s+(-1)**k/(2*k+1)
    return s

def tr_qa_increase(e):
    n=1
    while (Abs((pi-4*truncated_qa1(n)))).evalf() >= e:
        n=n+1
    return n

print(tr_qa_increase(0.012))