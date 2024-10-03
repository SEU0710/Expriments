import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = 1 / (1 + 1 / x)
plt.plot(x, y)
plt.show()