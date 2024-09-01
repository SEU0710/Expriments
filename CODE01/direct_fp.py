'''
Autor: Zhang Tianxiang
Date: 2024-08-30 21:17:27
LastEditors: Zhang Tianxiang
LastEditTime: 2024-08-31 15:38:03
'''
import numpy as np
import cvxpy as cvx
"""参数设置"""
car_num = 3  # 链路数
p_range = (0, 1)  # 功率范围
a = np.random.rand(car_num)+1  # 路径增益
print(a)
a_2 = np.sqrt(a)
m = np.random.rand(car_num) * 0.2  # 干扰路径增益
print(m)
w = np.ones(car_num)  # 权重
sigma2 = 0.5  # 噪声功率

p_init = np.ones(car_num) * np.mean(p_range)  # 初始值

p = [cvx.Variable() for i in range(car_num)]  # 变量：功率
# y = car_num  # 辅助变量
# 求干扰的和
p_next = np.zeros(car_num)
p_next = p_init
resu1 = 0
for i in range(10):
    dist_sum = np.array([np.sum(np.delete(p_next, i)) for i in range(car_num)])
    y = np.sqrt(a * p_next) / (dist_sum + sigma2)
    y2 = np.power(y, 2)
    i = 0
    obj = cvx.Maximize(w[0]*2*y[0]*a_2[0]*cvx.sqrt(p[0]) - w[0]*y2[0]*(m[1]*p[1]+m[2]*p[2]+sigma2) + w[1]*2*y[1]*a_2[1]*cvx.sqrt(p[1]) - w[1]*y2[1]*(m[0]*p[0]+m[2]*p[2]+sigma2) + w[2]*2*y[2]*a_2[2]*cvx.sqrt(p[2]) - w[2]*y2[2]*(m[0]*p[0]+m[1]*p[1]+sigma2))
    const0 = p[0] >= p_range[0]
    const1 = p[0] <= p_range[1]
    const2 = p[1] >= p_range[0]
    const3 = p[1] <= p_range[1]
    const4 = p[2] >= p_range[0]
    const5 = p[2] <= p_range[1]
    const = [const0, const1, const2, const3, const4, const5]
    prob = cvx.Problem(obj, const)
    resu = prob.solve()
    if np.abs(resu-resu1) < 0.00000000000001:
        break
    else:
        resu1 = resu
    print(resu)
    for j in range(car_num):    
        print(p[j].value)
        p_next[j] = p[j].value
    print('###')
    p = [cvx.Variable() for i in range(car_num)]  # 变量：功率
# [np.delete(cvx.multiply(m, p_ini), i) for i in range(num)]
# """迭代求解"""
# for t in range(1):
#     itf.value = np.array([np.sum(np.delete(cvx.multiply(m, p_ini), i)) for i in range(num)])
#     print(np.delete(cvx.multiply(m, p_ini), i))
#     y.value = np.sqrt(a * p_ini) / (itf + sigma2)
#     f = cvx.sum(w * (2*y*np.sqrt(a*p_ini)-y**2*(itf+sigma2)))
#     obj = cvx.Maximize(f)
#     const0 = p >= p_min
#     const1 = p <= p_max
#     const = [const0, const1]
#     problem = cvx.Problem(obj, const)
#     result = problem.slove()
#     print(result)
