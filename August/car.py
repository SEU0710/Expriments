'''
Autor: Zhang Tianxiang
Date: 2024-08-18 19:49:56
LastEditors: Zhang Tianxiang
LastEditTime: 2024-08-19 11:25:27
'''
"""
生成距离曲线
"""
import numpy as np
import matplotlib.pyplot as plt


def Fit_interp(coe, x):
    '''
    计算系数coe多项式在横坐标x处插值点值
    '''
    rank = np.size(coe) - 1
    result = 0
    for i in range(rank):
        result = result + coe[i]*np.power(x, rank-i)
    return result + coe[rank]


# 参数
dot_num  = 20  # 离散点数
time_len  = 10  # 时间长度/s
t = np.linspace(0, time_len, dot_num)  # 离散时间
random_var = np.random.rand(dot_num)  # dot_num/10个随机数据
fit_rank = 5  # 多项式阶数
coe = np.polyfit(t, random_var, fit_rank)  # 拟合random_var=f(t)
fit_result = [Fit_interp(coe, i) for i in t]  # 各点对应拟合结果
tt = np.linspace(0, time_len, int(2*dot_num))  # 插值点时间离散点
interp_result = np.interp(tt, t, fit_result)  # 插值后离散结果
# 绘图
fig, ax = plt.subplots()
ax.scatter(t, random_var)
ax.plot(t, fit_result)
ax.scatter(tt, interp_result)
# 显示
plt.show()