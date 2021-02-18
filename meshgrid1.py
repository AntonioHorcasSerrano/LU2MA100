import matplotlib.pyplot as plt
import numpy as np

x = [-3,-2,-1,0,1,2,3]
y = [1,2]
z = [7,5,6,5,1,0,9,5,3,8,3,1,0,4]
x_, y_ = np.meshgrid(x, y)
z_grid = np.array(z).reshape(2,7)
fig = plt.figure()
ax1 = plt.contour(x_,y_,z_grid)
plt.colorbar(ax1)
plt.show()