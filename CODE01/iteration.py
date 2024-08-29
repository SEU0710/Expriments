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
p = p_ini
sinr = 1
for i in range(10):
    sinr = a * p / (np.sum(m * p)+sigma2)
    sinr_m = np.sum(sinr)/num
    p_ite = (sinr - sinr_m) * p
    if sinr - sinr_last < err:
        break
    p = p_ite
    sinr_last = sinr
print('over')
