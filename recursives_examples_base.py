import numpy as np

# def fib(k):
#     if k == 1 or k == 0:
#         return k
#     else:
#         return  fib(k-1) + fib(k-2)

# print(fib(3))

# def factorielle(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorielle(n-1)

# factorielle(5)

# def suite(n):
#     # suite arithmétique de premier terme 5 et raison 2
#     print(n)
#     if n == 0:
#         return 5
#     else:
#         return suite(n-1) + 2
    

# print(suite(6))

def suite(n):
    # suite géométrique de premier terme 1 et raison 2
    if n == 0:
        return 1
    else:
        return suite(n-1) * 2

n=range(6)
print(sum(np.vectorize(suite)(n)))
