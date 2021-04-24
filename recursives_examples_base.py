# def gcd(p,q):
#     print(f'{p},{q}')
#     if q == 0: return p
#     return gcd(q, p % q)

# print (gcd(37,7))

# import numpy as np


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
 
def toString(List):
    return ''.join(List)
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print (toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
 
# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

def permute1(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute1(1, s)
                 for x in permute1(list - 1, s)
                 ]

print(permute1(1, ["a","b","c"]))
print(permute1(3, ["a","b","c"]))