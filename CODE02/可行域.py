import matplotlib.pyplot as plt
import numpy as np

"""超参数"""
P_v = 10  # dBm
G_0 = 30  # dBi
sigma = 30  # dBsm
epsilon = 0.1
theta = 15  # angle
D = 3.6  # m
M = 10
fc = 77e9  # Hz
C = 3e8  # m/s

"""计算边界"""
lamda_v = C / fc
epsiolon_1 = G_0 * G_0 * lamda_v ** 2 / (4 * np.pi) ** 2
epsiolon_2 = sigma / (4 * np.pi)
lamda_h = epsilon * roy
n = 5  # 对向
m = 5  # 同向
j = np.arange(1, n+1, 1)
i = 3
I_cci = np.sum(epsiolon_1 * lamda_h * P_v / ((m - i + j) * D) * np.tan(theta / 2))


"""绘图"""
plt.figure()
plt.plot()
# plt.show()

