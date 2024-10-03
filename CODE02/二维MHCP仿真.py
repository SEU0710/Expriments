import numpy as np
import matplotlib.pyplot as plt

# 初始化参数
lambd = 100  # 密度
M = 0
U = np.random.rand()

# 判定条件
while U >= np.exp(-lambd):
    U *= np.random.rand()
    M += 1

if M < 1:
    M = 1

# 生成点坐标
L = 100
a, b = 0, L
c, d = 0, L
A = np.zeros(M)  # 存储X坐标
B = np.zeros(M)  # 存储Y坐标

# 生成M个随机点坐标
for i in range(M):
    U1 = np.random.rand()  # 随机数1
    A[i] = (b - a) * U1  # X坐标
    U2 = np.random.rand()  # 随机数2
    B[i] = (d - c) * U2  # Y坐标
    plt.plot(A[i], B[i], 'r^')  # 绘制散点图
    #plt.hold(True)  # 保持绘图状态

plt.grid(True)  # 显示网格
Hppp = np.vstack((A, B))  # 将X坐标和Y坐标堆叠在一起

# 标记点
mark = np.random.rand(M)  # 生成M个随机标记
index = np.argsort(mark)  # 对标记进行排序
newmatrix = Hppp[:, index]  # 根据排序的索引重新排列点坐标

plt.figure(1)
plt.scatter(newmatrix[0], newmatrix[1], c='r', marker='^')  # 绘制散点图
plt.title('(a) HPPP')  # 设置标题
plt.grid(True)  # 显示网格

# 计算点之间的距离
distance = np.zeros((M, M))  # 初始化距离矩阵
for i in range(M):
    for j in range(i+1, M):
        # 计算欧氏距离
        distance[i, j] = np.sqrt(np.sum((newmatrix[:, i] - newmatrix[:, j])**2))
distance = distance + distance.T  # 对称距离矩阵

# 距离判别
disth = 8  # 设定判别门限
indexpoint = np.ones(M)  # 初始化标记点
dis = distance >= disth  # 生成距离判别矩阵

for i in range(M):
    for j in range(i+1, M):
        if indexpoint[i] == 1:
            if dis[i, j] == 0:
                indexpoint[j] = 0

temp = np.where(indexpoint == 1)[0]  # 筛选符合条件的点索引

# 生成 MHCPP 图
Mhcpp = newmatrix[:, temp]  # 筛选出符合条件的点坐标
plt.figure(2)
plt.scatter(Mhcpp[0], Mhcpp[1], c='r', marker='^')  # 绘制 MHCPP 图
plt.title('(b) MHCPP with disth='+str(disth))  # 设置标题
plt.grid(True)  # 显示网格
plt.show()  # 展示图形
