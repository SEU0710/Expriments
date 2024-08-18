import numpy as np
import matplotlib.pyplot as plt

# 参数
v0 = np.arange(10)
v1 = np.arange(-1, 4, 0.5)

# 绘图
fig, ax = plt.subplots()
ax.stem(v0)
ax.stem(v1)
# 显示
plt.show()