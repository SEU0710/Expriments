#FMCW体制
fc = 77e9  # 77GHz
B = 150e6  # 150MHz
T = 2e-3  # 2ms
ac = 8  # 脉冲累积数8
k = B/T

a = 1 # 电平
import numpy as np
t = np.arange(-T/2, T/2, 1/(2*B))
w = a * np.exp(1j*np.pi*k*t**2)

w_f = np.tile(w, ac)

# 雷达距离方程



# 绘图
import matplotlib.pyplot as plt
plt.figure()
plt.specgram(w_f, Fs=2*B)
plt.show()
