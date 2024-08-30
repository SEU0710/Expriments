'''
Autor: Zhang Tianxiang
Date: 2024-08-30 21:17:27
LastEditors: Zhang Tianxiang
LastEditTime: 2024-08-30 22:00:46
'''
import numpy as np
"""参数设置"""
num = 4
p_min = 0
p_max = 10
a = np.random.rand(num)
p_ini = np.ones(num) * (p_min+p_max)/2
m = np.random.rand(num) * 0.2
sigma2 = 2
"""迭代求解"""
for i in range(10):
    interfare = np.array([np.sum(np.delete(m*p_ini, i)) for i in range(num)])
    y = np.sqrt(a * p_ini) / (interfare + sigma2)
    print(y)
