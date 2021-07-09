import matplotlib.pyplot as plt
import numpy as np

k1 = 1
k2 = 2
x = np.linspace(-10, 10, 121)
plt.plot(x, k1* np.cos(x))
plt.plot(x, k2* np.cos(x))
plt.show()


