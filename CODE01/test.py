'''
Autor: Zhang Tianxiang
Date: 2024-09-01 13:22:21
LastEditors: Zhang Tianxiang
LastEditTime: 2024-09-05 02:28:39
'''
import cvxpy as cvx
import numpy as np

P_ = np.ones((3,1))

H = np.asarray([[0.1, 0.02, 0.01], [0.02, 0.2, 0.01], [0.02, 0.01, 0.15]])

H_diag = np.diag(np.diag(H))

sig2 = 1

for i in range(100):
#     y2 = np.sqrt(0.6*p2_) / (0.6*p3_ + 0.1)
#     y3 = np.sqrt(1.8*p3_) / (0.6*p2_ + 0.1)
    y = np.sqrt(H * P_) / ((H - H_diag) * P_ + sig2)
#     print(y2,y3)
#     p2 = cvx.Variable(pos=True)
#     p3 = cvx.Variable(pos=True)
    P = cvx.Variable((3,1))
    #fuc = p2 / (0.6 * p3 + 0.1) + 1.8 * p3 / (0.6 * p2 + 0.1)
#     fuc = 0.5*(2 * y2 * cvx.sqrt(0.6 * p2) - np.power(y2, 2) * (0.6 * p3 + 0.1)) + \
#             0.5*(2 * y3 * cvx.sqrt(1.8 * p3) - y3**2 * (0.6 * p2 + 0.1))
    fuc = cvx.sum(2*y @ cvx.sqrt(H_diag @ P) - y**2 @ ((H - H_diag) @ P + sig2))
    obj = cvx.Maximize(fuc)
#     cst1 = p2 >= 0
#     cst2 = p3 >= 0
#     cst = [cst1, cst2]
#     cst1 = P[0] >= 0
#     cst2 = P[1] >= 0
#     cst3 = P[0] <= 10
#     cst4 = P[1] <= 10
    cst1 = P >= 0
    cst2 = P <= 10
    #cst = [cst1, cst2, cst3, cst4]
    cst = [cst1, cst2]
    prob = cvx.Problem(obj, cst)
    # rsl = prob.solve(solver='ECOS')
    rsl = prob.solve()
    print(rsl)
    print(P.value)
    print("######")
    P_ = P.value