import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-3, 3, 1)
y = np.arange(-3, 3, 1)
# i = np.zeros((2, 3, 4))
# print(i)
xx, yy = np.meshgrid(x, y)
print(xx)
print(yy)
z=xx+yy
print(z)
z = np.sin(xx)+np.sin(yy)
print(type(z))
print(z.shape)
plt.plot(xx,yy, marker='.', color='k', linestyle='none')
h = plt.contour(xx,yy,z)
plt.colorbar(h)
for l in range(6):
    for c in range(6):
        print(f'{xx[l][c]},{yy[l][c]},{z[l][c]}')
plt.show()

# x,y,z
# -2,-2,-1.82
# -1,-2,-1.75
# -2,-1,-1.75
# -1,-1,-1.68
# -2,-3,-1.05
# -3,-2,-1.05
# -1,-3,-0.98
# -3,-1,-0.98
# 0,-2,-0.91
# -2,0,-0.91
# 0,-1,-0.84
# -1,0,-0.84
# -3,-3,-0.28
# 0,-3,-0.14
# -3,0,-0.14
# 1,-2,-0.07
# -2,1,-0.07
# 2,-2,0.00
# 1,-1,0.00
# 0,0,0.00
# -1,1,0.00
# -2,2,0.00
# 2,-1,0.07
# -1,2,0.07
# 1,-3,0.70
# -3,1,0.70
# 2,-3,0.77
# -3,2,0.77
# 1,0,0.84
# 0,1,0.84
# 2,0,0.91
# 0,2,0.91
# 1,1,1.68
# 2,1,1.75
# 1,2,1.75
# 2,2,1.82