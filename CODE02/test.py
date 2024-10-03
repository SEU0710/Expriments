import numpy as np
import matplotlib.pyplot as plt
lamda = np.linspace(0, 100, 10000)
r = 10
plt.plot(1-np.exp(-2 * lamda * r))
plt.show()