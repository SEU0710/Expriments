'''
Autor: Zhang Tianxiang
Date: 2024-08-20 12:44:01
LastEditors: Zhang Tianxiang
LastEditTime: 2024-08-20 13:40:34
'''
import numpy as np
import matplotlib.pyplot as plt

dot_num = 1000  # 一百次采样
action_num = 100
acc = np.random.choice((-2, -1, 0, 1, 2), action_num)  # 10次加减速动作
acc2 = np.random.choice((-2, -1, 0, 1, 2), action_num)  # 10次加减速动作
print(acc)
print(acc2)
t = np.linspace(0, 100, action_num)
tt = np.linspace(0, 100, dot_num)
acc_i = acc.repeat(int(dot_num/action_num))  # 
acc2_i = acc2.repeat(int(dot_num/action_num))  # 
v = []
v2 = []
v_init = 40
for i in range(dot_num):
    v.append(np.trapz(acc_i[:i+1], tt[:i+1])+40)
    v2.append(np.trapz(acc2_i[:i+1], tt[:i+1])+40)
d = []
d2 = []
dd = []
d_init = 10
for i in range(dot_num):
    d.append(np.trapz(v[:i+1], tt[:i+1]))
    d2.append(np.trapz(v2[:i+1], tt[:i+1]))
    dd.append(np.trapz(v[:i+1], tt[:i+1]) - np.trapz(v2[:i+1], tt[:i+1]) + d_init)
fig, ax = plt.subplots()
ax.plot(tt, acc_i)
ax.plot(tt, v)
ax.legend(['a','v'])
fig, ax2 = plt.subplots()
ax2.plot(tt, acc2_i)
ax2.plot(tt, v2)
ax2.legend(['a2','v2'])
fig, ax3 = plt.subplots()
# ax3.plot(tt, d)
# ax3.plot(tt, d2)
ax3.plot(tt, np.abs(dd))
# ax3.legend(['d','d2', 'dd'])
plt.show()


