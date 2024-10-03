import matplotlib.pyplot as plt
import numpy as np

# Parameters
pt_v = 10  # (dBm)
theta = 15  # (deg)
C = 3e8  # light velocity (m)
fc = 76.5  # (GHz)
Gt_v = 30  # antenna gain (dBi)
sigma = 30  # (dBsm)

# transform unit
pt_v = 10 ** (pt_v / 10)  # (mW)
theta = theta * np.pi / 180  # (rad/s)
fc = fc * 1e9  # (Hz)
Gt_v = 10 ** (Gt_v / 10)
sigma = 10 ** (sigma / 10)

lamda = C / fc  # wave length (m)

# simulation variables
epsilon = 0.1
D = 3.6  # (m)
d_h = 10  # (m)
road_len = 1e3  # (m)

"""计算边界"""
lamda_v = C / fc
varepsilon_1 = (Gt_v * lamda_v / (4 * np.pi)) ** 2
varepsilon_2 = sigma / (4 * np.pi)
rho_i = 100
rho_h = (1 - np.exp(-2 * epsilon * rho_i / road_len * d_h)) / (2 * d_h) # MHCP density
I_the = varepsilon_1 * rho_h * pt_v * np.tan(theta / 2) / D
n = 5  # 对向
m = 5  # 同向
j = np.arange(1, n+1, 1)
i = 3
# I_cci = np.sum(varepsilon_1 * lamda_h * P_v / ((m - i + j) * D) * np.tan(theta / 2))
# 边界
rv_th = 0.001
ru_th = 0.001
R_v = 105
R_u = 200
N0 = 1e-17 * 1e9
a_v = rv_th * N0 / (varepsilon_1*varepsilon_2 / (R_v**4) - rv_th*I_the/pt_v)
a_u = ru_th * N0 / (varepsilon_1*varepsilon_2 / (R_u**4))
print(a_v)
print(a_u)

P = 0.050 # 50 mW
P_v = np.linspace(0, P, 100)
P_u = []
for p_v in P_v:
    P_u.append(ru_th * N0 / (rv_th*I_the/pt_v + rv_th*N0/p_v))


"""绘图"""
plt.figure()
plt.plot(P_v, P_u)
plt.plot([a_v, a_v], [0, 1])
plt.plot([0, 1], [a_u, a_u])
plt.plot(np.arange(10)*0.1, P-np.arange(10)*0.1)
plt.xlim([-0.1*P, 1.2*P])
plt.ylim([-0.1*P, 1.2*P])
plt.show()

