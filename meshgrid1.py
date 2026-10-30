import matplotlib.pyplot as plt
import numpy as np
from itertools import product

x = [-3,-2,-1,0,1,2,3]
y = [1,2]
z = [0,1,0,1,0,1,0,1,0,1,0,1,0,1]
p = product(x,y)
x__,y__ = zip(*p)
x_, y_ = np.meshgrid(x, y)
print(x_)
print(y_)
z_grid = np.array(z).reshape(2,7)
print(z_grid)
fig = plt.figure()
plt.plot(x__,y__, marker='*', color='g', linestyle='none')
plt.plot(x_,y_, marker='.', color='k', linestyle='none')
# ax1 = plt.contour(x_,y_,z_grid)
# plt.colorbar(ax1)
plt.show()