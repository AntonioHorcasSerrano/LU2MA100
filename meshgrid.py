import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-5, 5, 1)
y = np.arange(-5, 5, 1)
xx, yy = np.meshgrid(x, y)
z = (-1/5)*yy+np.e**(-xx**2-yy**2)
plt.plot(xx,yy, marker='.', color='k', linestyle='none')
h = plt.contour(xx,yy,z)
plt.show()