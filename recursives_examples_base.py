# def gcd(p,q):
#     print(f'{p},{q}')
#     if q == 0: return p
#     return gcd(q, p % q)

# print (gcd(37,7))
def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
A = [12, 24, 27, 30, 36]
res = A[0]
for c in A[1::]:
    res = gcd(res , c)
print(res)
# import numpy as np

# Combinaisons recursive (calcul des coefficients binomiaux)

# http://pythontutor.com/visualize.html#code=def%20combin%28n,k%29%3A%0A%20%20%20%20%22%22%22Nombre%20de%20combinaisons%20de%20n%20objets%20pris%20k%20a%20k%20%28calcul%20r%C3%A9cursif%29%22%22%22%0A%20%20%20%20if%20k%3D%3D0%20or%20k%3D%3Dn%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20a%20%3D%20combin%28n-1,%20k-1%29%0A%20%20%20%20b%20%3D%20combin%28n-1,k%29%0A%20%20%20%20print%28f'%28%7Bn%7D,%7Bk%7D%29,%7Ba%2Bb%7D'%29%0A%20%20%20%20return%20a%2Bb%0Acombin%284,2%29&cumulative=false&curInstr=59&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# http://pythontutor.com/visualize.html#code=def%20fib%28k%29%3A%0A%20%20%20%20if%20k%20%3D%3D%201%20or%20k%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20k%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20fib%28k-1%29%20%2B%20fib%28k-2%29%0Afib%285%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# def fib(k):
#     if k == 1 or k == 0:
#         return k
#     else:
#         return fib(k-1) + fib(k-2)

# print(fib(4))

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

# def suite(n):
#     # suite géométrique de premier terme 1 et raison 2
#     if n == 0:
#         return 1
#     else:
#         return suite(n-1) * 2

# n=range(6)
# print(sum(np.vectorize(suite)(n)))

# Python program to print all permutations with
# duplicates allowed
 
# def toString(List):
#     return ''.join(List)
 
# # Function to print permutations of string
# # This function takes three parameters:
# # 1. String
# # 2. Starting index of the string
# # 3. Ending index of the string.
# def permute(a, l, r):
#     if l==r:
#         print (toString(a))
#     else:
#         for i in range(l,r+1):
#             a[l], a[i] = a[i], a[l]
#             permute(a, l+1, r)
#             a[l], a[i] = a[i], a[l] # backtrack
 
# Driver program to test the above function
# string = "ABC"
# n = len(string)
# a = list(string)
# permute(a, 0, n-1)

# def permute1(list, s):
#     if list == 1:
#         return s
#     else:
#         return [ y + x
#                  for y in permute1(1, s)
#                  for x in permute1(list - 1, s)
#                  ]

# print(permute1(2, ["a","b","c"]))
# print(permute1(4, ["a","b","c"]))

# def z(n, c=0):
#     if n == 0:
#         return 0+0j
#     else:
#         return z(n-1,c) * z(n-1,c) +  c
# print(z(3, 1+1j))

# def syracuse(n):
#     if n == 1:
#         return [1]
#     elif n % 2:
#         return [n] + syracuse(n/2)
#     else:
#         return [n] + syracuse(n*3+1)