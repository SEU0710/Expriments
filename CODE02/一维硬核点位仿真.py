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
m = 3  # 车道数

# 路面绘图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(10, 4))
plt.title("硬核PPP随机点位模拟")
# 路边
for i in range(m):
    plt.plot([0, road_len], [D*(0.5+i), D*(0.5+i)], color='gray', zorder=1)
# 中线
for i in range(m+1):
    plt.plot([0, road_len], [i*D, i*D], color='lightgray', linestyle='--', zorder=1)
# 受害车辆
plt.scatter([0], [0], s=10, marker='s', linewidths=1, edgecolors='black', zorder=3)
# 波束边界
plt.plot([0, road_len], [0, road_len*np.tan(theta/2)], color='black', linestyle=':', zorder=2)

# sim
lane = [3.6, 7.2, 10.8]
rho = np.linspace(10, 100, 10)  # endpoint 'True'
rho_i = 10
print('initial vehicle density: ' + str(rho_i / road_len))
for D in lane:
    p_num = np.random.poisson(rho_i)
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
    # 绘制点位
    plt.scatter(p_mhcp, D * np.ones_like(p_mhcp), s=10, marker='s', linewidths=1,
                edgecolors='black', zorder=3)

# 其他
plt.ylim(-1.8, 12.6)
plt.ylabel('$l$/m')
plt.xlabel('$d$/m')
plt.show()
