import numpy as np
import matplotlib.pyplot as plt

# def mandelbrot(c):
#     """ Rend True ou False si c appartient à l'ensemble ou non, respectivement
#     """
#     z = 0j
#     for _ in range(99):
#         if abs(z) > 2.0:
#             return False
#         z = z**2 + c
#     return True

# def tab():
#     N = 300
#     lst = np.linspace(-2,2,N)
#     x, y = np.meshgrid(lst,lst)
#     c = x + 1j*y
#     out = np.empty([N, N], dtype=bool)
#     for i in range(N):
#         for j in range(N):
#             if mandelbrot(c[i,j]):
#                 out[i,j] = True
#             else:
#                 out[i,j] = False
#     G = np.zeros((N,N,3))
#     G[out == True] = [1,1,1]
#     G[out == False] = [0,0,0]
#     plt.imshow(G)
#     plt.show()
#     return out
# print(tab())
import matplotlib.pyplot as plt
import numpy as np

# cnums = np.arange(5) + 1j * np.arange(6,11)
# X = [x.real for x in cnums]
# Y = [x.imag for x in cnums]
# plt.scatter(X,Y, color='red')
# plt.show()

xx = np.linspace(-2,2,5)
yy = np.linspace(-2,2,5)
print(xx)
print(yy)
plt.scatter(xx,yy, color='red')
xxx, yyy = np.meshgrid(xx, yy)
z = xxx + yyy * 1j
print(np.angle(z))
h = plt.imshow(np.angle(z))
plt.colorbar(h)
plt.show()

a = np.arange(5) + 1j*np.arange(6,11)
for x in a:
    plt.polar([0,np.angle(x)],[0,abs(x)],marker='o')
plt.show()