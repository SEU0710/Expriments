"""
生成距离曲线
"""
import numpy as np
import matplotlib.pyplot as plt

# 参数
t = np.arange(10)
d = np.random.rand(10)
c = np.polyfit(t, d, 4)
func = [c[0]*i**4 + c[1]*i**3 + c[2]*i**2 + c[3]*i + c[4] for i in t]
tt = np.arange(0, 10, 0.2)
y = np.interp(tt, t, func)
# 绘图
fig, ax = plt.subplots()
ax.scatter(t, d)
ax.plot(t, func)
ax.scatter(tt, y)
# 显示
plt.show()