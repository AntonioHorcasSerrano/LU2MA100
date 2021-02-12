import numpy as np
import matplotlib.pyplot as plt
xlist = np.linspace(-3.0, 3.0, 100)
ylist = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = (-1/5)*Y+np.e**(-X**2-Y**2)
fig,ax=plt.subplots(1,1)
cp = ax.contour(X, Y, Z)
fig.colorbar(cp) # Add a colorbar to a plot
ax.set_title('Contours Plot')
ax.set_ylabel('y')
plt.show()