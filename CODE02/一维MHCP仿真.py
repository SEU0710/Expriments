from pydoc import locate

import numpy as np
import matplotlib.pyplot as plt
from skimage.color.rgb_colors import linen

road_len = 1000

lamda = 100
print(lamda / road_len)

epsilon = 0.1

r = 10

D = 3.6

# 硬核概率密度
lamda_h = (1-np.exp(-2*epsilon*lamda*r/road_len))/(2*r)
# lamda_h = lamda_h * epsilon
print(lamda_h)

calo = 100000
I_ = []
I_sim_ = []
for lamda in [10,20,30,40,50,60,70,80,90,100]:

    lamda_h = (1 - np.exp(-2 * epsilon * lamda * r / road_len)) / (2 * r)

    I_sim = 0
    for k in range(calo):
        p_num = np.random.poisson(lamda * epsilon)
        p_x = np.random.rand(p_num)
        p_x_road = p_x * road_len
        p_x_road_sort = np.sort(p_x_road)
        p_x_road_sort_thinned = []
        i, j = 0, 0
        try:
            p_x_road_sort_thinned.append(p_x_road_sort[0])
            while i < p_num:  # 筛选
                if p_x_road_sort[i] - p_x_road_sort[j] >= r:
                    p_x_road_sort_thinned.append(p_x_road_sort[i])
                    j = i
                i += 1
        except:
            pass

        # p_num = np.random.poisson(lamda)
        # p_x = np.random.rand(p_num)
        # p_x_road = p_x * road_len
        # p_x_road_sort = np.sort(p_x_road)
        # p_x_road_sort_thinned1 = []
        # i, j = 0, 0
        # p_x_road_sort_thinned1.append(p_x_road_sort[0])
        # while i < p_num:  # 筛选
        #     if p_x_road_sort[i] - p_x_road_sort[j] >= r:
        #         p_x_road_sort_thinned1.append(p_x_road_sort[i])
        #         j = i
        #     i += 1
        #
        # p_num = np.random.poisson(lamda)
        # p_x = np.random.rand(p_num)
        # p_x_road = p_x * road_len
        # p_x_road_sort = np.sort(p_x_road)
        # p_x_road_sort_thinned2 = []
        # i, j = 0, 0
        # p_x_road_sort_thinned2.append(p_x_road_sort[0])
        # while i < p_num:  # 筛选
        #     if p_x_road_sort[i] - p_x_road_sort[j] >= r:
        #         p_x_road_sort_thinned2.append(p_x_road_sort[i])
        #         j = i
        #     i += 1

        # 计算干扰
        pt_v = 10e-3
        theta = 15 * np.pi / 180
        C = 3e8
        fc = 76.5e9
        lamda_v = C / fc
        Gt_v, Gr_v = 1e3, 1e3
        sigma_1 = Gt_v * Gr_v * lamda_v**2 / (4*np.pi)**2
        # I = sigma_1 * lamda * epsilon / road_len * pt_v * np.tan(theta / 2) / D
        I = sigma_1 * lamda_h * pt_v * np.tan(theta / 2) / D
        # print(I)
        delta = 1e3
        sigma_2 = delta / (4 * np.pi)
        # I_sim = 0
        # x_v = np.random.choice(p_x_road_sort_thinned, int(0.1 * np.size(p_x_road_sort_thinned)))
        # for x_ in x_v:
        for x_ in p_x_road_sort_thinned:
            if x_ > D / np.tan(theta / 2):
                R_v_2 = 1 / (x_**2 + D**2)
                I_sim = I_sim + R_v_2

    I_sim = sigma_1 * pt_v * I_sim / calo
    I_.append(I)
    I_sim_.append(I_sim)
    print(I)
    print(I_sim)

roy = np.arange(0.01, 0.11, 0.01)
plt.plot(roy, I_)
plt.scatter(roy, I_sim_)
# # 绘图
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.figure(figsize=(10, 4))
# plt.title("硬核PPP随机点位模拟")
# # 路基
# plt.plot([0, 500], [1.8, 1.8], color='gray', zorder=1)
# plt.plot([0, 500], [1.8+3.6, 1.8+3.6], color='gray', zorder=1)
# plt.plot([0, 500], [1.8+3.6*2, 1.8+3.6*2], color='gray', zorder=1)
# # 中线
# plt.plot([0, 500], [0, 0], color='lightgray', linestyle='--', zorder=1)
# plt.plot([0, 500], [3.6, 3.6], color='lightgray', linestyle='--', zorder=1)
# plt.plot([0, 500], [2*3.6, 2*3.6], color='lightgray', linestyle='--', zorder=1)
# plt.plot([0, 500], [3*3.6, 3*3.6], color='lightgray', linestyle='--', zorder=1)
# # 车辆
# # plt.scatter(p_x_road_sort, np.zeros_like(p_x_road_sort), s=10, marker='s', linewidths=1, edgecolors='black')
# plt.scatter([0], [0], s=10, marker='s', linewidths=1, edgecolors='black', zorder=3)
# plt.scatter(p_x_road_sort_thinned, D*np.ones_like(p_x_road_sort_thinned), s=10, marker='s', linewidths=1, edgecolors='black', zorder=3)
# plt.scatter(p_x_road_sort_thinned1, 2*D*np.ones_like(p_x_road_sort_thinned1), s=10, marker='s', linewidths=1, edgecolors='black', zorder=3)
# plt.scatter(p_x_road_sort_thinned2, 3*D*np.ones_like(p_x_road_sort_thinned2), s=10, marker='s', linewidths=1, edgecolors='black', zorder=3)
# # 视角
# theta = 15 * np.pi / 180
# plt.plot([0, 500], [0, 500*np.tan(theta/2)], color='black', linestyle=':', zorder=2)
# # 其他
# plt.ylim(-1.8, 12.6)
# plt.ylabel('$l$/m')
# plt.xlabel('$d$/m')
plt.show()




# plt.figure(1)
# plt.plot(p)
# plt.figure(2)
# plt.plot(x)
plt.show()