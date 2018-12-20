import matplotlib.pyplot as plt
import numpy as np

#lovely contour

y, x = np.ogrid[-1:2:100j, -1:1:100j]
plt.contour(x.ravel(), 
            y.ravel(), 
            x**2 + (y-((x**2)**(1.0/3)))**2, 
            [1],
            colors='red',)
plt.axis('equal')
plt.show()
