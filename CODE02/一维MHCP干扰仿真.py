import numpy as np
import matplotlib.pyplot as plt

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
monte_carlo = 10000

# sim
lane = [3.6, 7.2, 10.8]
rho = np.linspace(10, 100, 10)  # endpoint 'True'
for D in lane:
    I_the_dat = []
    I_sim_dat = []
    for rho_i in rho:
        rho_h = (1 - np.exp(-2 * epsilon * rho_i / road_len * d_h)) / (2 * d_h) # MHCP density
        # rho_h = epsilon * (1 - np.exp(-2 * rho_i / road_len * d_h)) / (2 * d_h)  # MHCP density
        print('initial vehicle density: ' + str(rho_i / road_len))
        print('MHCP vehicle density: ' + str(rho_h))
        # 理论干扰
        varepsilon = (Gt_v * lamda / (4 * np.pi)) ** 2
        I_the = varepsilon * rho_h * pt_v * np.tan(theta / 2) / D
        I_the_dat.append(I_the)
        # 仿真干扰
        I_sim = 0
        for t in range(monte_carlo):  # mean
            p_num = np.random.poisson(epsilon * rho_i)
            p_coor = np.random.rand(p_num) * road_len  # point coordinate
            p_sort = np.sort(p_coor)
            p_mhcp = []
            i, j = 0, 0
            try:
                p_mhcp.append(p_sort[0])
                while i < p_num:  # 筛选
                    if p_sort[i] - p_sort[j] >= d_h:
                        p_mhcp.append(p_sort[i])
                        j = i
                    i += 1
            except Exception:
                pass
            # 计算干扰
            for p_x in p_mhcp:
                if p_x > D / np.tan(theta / 2):
                    Rv_2 = 1 / (p_x**2 + D**2)
                    I_sim = I_sim + Rv_2
        I_sim_dat.append(varepsilon * pt_v * I_sim / monte_carlo)

    ro = np.arange(0.01, 0.11, 0.01)
    plt.plot(ro, I_the_dat)
    plt.scatter(ro, I_sim_dat)
plt.show()

# 绘图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(10, 4))
plt.title("硬核PPP随机点位模拟")
# 路基
plt.plot([0, 500], [1.8, 1.8], color='gray', zorder=1)
plt.plot([0, 500], [1.8+3.6, 1.8+3.6], color='gray', zorder=1)
plt.plot([0, 500], [1.8+3.6*2, 1.8+3.6*2], color='gray', zorder=1)
# 中线
plt.plot([0, 500], [0, 0], color='lightgray', linestyle='--', zorder=1)
plt.plot([0, 500], [3.6, 3.6], color='lightgray', linestyle='--', zorder=1)
plt.plot([0, 500], [2*3.6, 2*3.6], color='lightgray', linestyle='--', zorder=1)
plt.plot([0, 500], [3*3.6, 3*3.6], color='lightgray', linestyle='--', zorder=1)
# 车辆
# plt.scatter(p_x_road_sort, np.zeros_like(p_x_road_sort), s=10, marker='s', linewidths=1, edgecolors='black')
plt.scatter([0], [0], s=10, marker='s', linewidths=1, edgecolors='black', zorder=3)
plt.scatter(p_x_road_sort_thinned, D*np.ones_like(p_x_road_sort_thinned), s=10, marker='s', linewidths=1, edgecolors='black', zorder=3)
plt.scatter(p_x_road_sort_thinned1, 2*D*np.ones_like(p_x_road_sort_thinned1), s=10, marker='s', linewidths=1, edgecolors='black', zorder=3)
plt.scatter(p_x_road_sort_thinned2, 3*D*np.ones_like(p_x_road_sort_thinned2), s=10, marker='s', linewidths=1, edgecolors='black', zorder=3)
# 视角
theta = 15 * np.pi / 180
plt.plot([0, 500], [0, 500*np.tan(theta/2)], color='black', linestyle=':', zorder=2)
# 其他
plt.ylim(-1.8, 12.6)
plt.ylabel('$l$/m')
plt.xlabel('$d$/m')
plt.show()