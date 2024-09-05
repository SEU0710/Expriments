'''
Autor: Zhang Tianxiang
Date: 2024-09-01 13:22:21
LastEditors: Zhang Tianxiang
LastEditTime: 2024-09-05 14:59:48
'''
import cvxpy as cvx
import numpy as np

num = 9
P_ = np.ones((num, 1)) * 0.1
pp = []
H = np.random.rand(num, num) + np.diag(np.ones(num))
H = 0.1 * H
H_diag = np.diag(np.diag(H))

sig2 = 0.1
for i in range(15):
    y = np.sqrt(H_diag * P_) / ((H - H_diag) * P_ + sig2)
    P = cvx.Variable((num, 1))
    fuc = cvx.sum(2*y @ cvx.sqrt(H_diag @ P) - y**2 @ ((H - H_diag) @ P + sig2))
    obj = cvx.Maximize(fuc)
    cst1 = P >= 0
    cst2 = P <= 10
    cst = [cst1, cst2]
    prob = cvx.Problem(obj, cst)
    rsl = prob.solve()
    s = np.sum(H_diag * P_ / ((H - H_diag) * P_ + sig2))
    pp.append(s)
    print(P.value)
    P_ = P.value

import matplotlib.pyplot as plt
plt.plot(pp)
plt.show()