import matplotlib.pyplot as plt
import numpy as np

gaussian_numbers = np.random.normal(size=10000)

plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
