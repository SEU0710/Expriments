'''
Autor: Zhang Tianxiang
Date: 2024-09-01 13:22:21
LastEditors: Zhang Tianxiang
LastEditTime: 2024-09-05 23:09:51
'''
import cvxpy as cvx
import numpy as np

num = 6
P_ = np.ones((num, 1)) * 0.5
ss = []
pp = []
pp1 = []
pp2 = []
pp3 = []
pp4 = []
pp5 = []
H = np.random.rand(num, num) + np.diag(np.ones(num))
# H = 0.1 * H
H_diag = np.diag(np.diag(H))
#print(np.shape(np.sqrt(H_diag @ P_)))
tt1 = []
tt2 = []
tt3 = []
tt4 = []
tt5 = []
tt6 = []
sig2 = 0.2
for i in range(20):
    tt1.append(P_[0])
    tt2.append(P_[1])
    tt3.append(P_[2])
    tt4.append(P_[3])
    tt5.append(P_[4])
    tt6.append(P_[5])
    s = H_diag @ P_ / ((H - H_diag) @ P_ + sig2)
    ss.append(np.sum(s))
    pp.append(s[0])
    pp1.append(s[1])
    pp2.append(s[2])
    pp3.append(s[3])
    pp4.append(s[4])
    pp5.append(s[5])
#     print(i)
#     print((H - H_diag) @ P_)
#     print(cvx.sqrt(H_diag @ P_))
    y = cvx.sqrt(H_diag @ P_) / ((H - H_diag) @ P_ + sig2)
    y = y.T
    P = cvx.Variable((num, 1))
    fuc = 2*y @ cvx.sqrt(H_diag @ P) - cvx.power(y, 2) @ ((H - H_diag) @ P + sig2)
    obj = cvx.Maximize(fuc)
    cst1 = P >= 0
    cst2 = P <= 1
    cst3 = cvx.multiply(H_diag @ P, cvx.power(((H - H_diag) @ P_ + sig2), -1)) >= 0.2
    cst = [cst1, cst2, cst3]
    prob = cvx.Problem(obj, cst)
    rsl = prob.solve()
    P_ = P.value
#     print(i,'##################3')
#     print(P.value)
#     print(s)
import matplotlib.pyplot as plt
plt.figure()
plt.plot(ss)
plt.figure()
plt.plot(pp)
plt.plot(pp1)
plt.plot(pp2)
plt.plot(pp3)
plt.plot(pp4)
plt.plot(pp5)

plt.figure()
plt.plot(tt1)
plt.plot(tt2)
plt.plot(tt3)
plt.plot(tt4)
plt.plot(tt5)
plt.plot(tt6)
plt.show()