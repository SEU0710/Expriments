'''
Autor: Zhang Tianxiang
Date: 2024-08-30 21:17:27
LastEditors: Zhang Tianxiang
LastEditTime: 2024-08-31 11:04:15
'''
import numpy as np
"""参数设置"""
num = 4
p_min = 0
p_max = 10
a = np.random.rand(num)
p_ini = np.ones(num) * (p_min+p_max)/2
m = np.random.rand(num) * 0.2
w = np.ones(num)
sigma2 = 2
"""迭代求解"""
for i in range(10):
    itf = np.array([np.sum(np.delete(m*p_ini, i)) for i in range(num)])
    y = np.sqrt(a * p_ini) / (itf + sigma2)
    f = np.sum(w * (2*y*np.sqrt(a*p_ini)-y**2*(itf+sigma2)))
    print(f)
