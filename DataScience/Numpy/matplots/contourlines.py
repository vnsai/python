import numpy as np


#Contour lines are used e.g. in geography and meteorology.


xlist = np.linspace(-3.0, 3.0, 3)
ylist = np.linspace(-3.0, 3.0, 4)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)
print(Z)

import matplotlib.pyplot as plt

plt.figure()
cp = plt.contour(X, Y, Z)
#cp = plt.contour(X, Y, Z, colors='black', linestyles='dashed')

plt.clabel(cp, inline=True, 
          fontsize=10)
plt.title('Contour Plot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()
