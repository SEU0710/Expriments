'''
Autor: Zhang Tianxiang
Date: 2024-08-20 12:44:01
LastEditors: Zhang Tianxiang
LastEditTime: 2024-08-20 13:04:32
'''
import numpy as np
import matplotlib.pyplot as plt

dot_num = 100  # 一百次采样
action_num = 10
acc = np.random.choice((-2, -1, 0, 1, 2), action_num)  # 10次加减速动作
t = np.arange(0, 100, 10)
tt = np.arange(0, 100, 1)
acc_i = acc.repeat(int(dot_num/action_num))  # 
v = []
for i in range(dot_num):
    v.append(np.trapz(acc_i[:i+1], tt[:i+1]))
d = []
for i in range(dot_num):
    d.append(np.trapz(v[:i+1], tt[:i+1]))
fig, ax = plt.subplots()
ax.plot(tt, acc_i)
ax.plot(tt, v)
ax.plot(tt, d)
ax.legend(['a','v','c'])
plt.show()


