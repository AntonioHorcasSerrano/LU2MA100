import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-3, 3, 1)
y = np.arange(-3, 3, 1)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx)+np.sin(yy)
plt.plot(xx,yy, marker='.', color='k', linestyle='none')
h = plt.contour(xx,yy,z)
plt.colorbar(h)
print(z.T)
plt.show()