import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 500, 1000)
y= np.cumsum(np.power(1/2, x)*x)

# print(y[-1])

plt.plot(x, y)

plt.legend()

plt.show()
