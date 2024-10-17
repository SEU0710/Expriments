from demo import *

def mean_interference_the(rho_i, epsilon=0.1):
    rho_h = (1 - np.exp(-2 * epsilon * rho_i / L * dh)) / (2 * dh)
    varepsilon = (d2b(Gv) * lamda_v / (4 * np.pi)) ** 2
    # I_the = varepsilon * rho_h * Pt_v * np.tan(d2r(theta) / 2) / dw  # 近似
    I_the = varepsilon * rho_h * Pt_v * (np.pi / 2 - np.arctan(1 / np.tan(d2r(theta) / 2))) / dw  # 非近似
    return I_the

def mean_interference_sim(rho_i, cola:int, epsilon=0.1):
    I = 0
    for i in range(cola):  # 蒙特卡洛次数
        v_x = vehicle_distribution(rho_i, L, dh, epsilon)
        v_d = facing_vehicle_distance(v_x, dw, d2r(theta))
        Iv_v = radar_recv_power(v_d, Pt_v, coe=(d2b(Gv) * lamda_v / (4 * np.pi)) ** 2)
        I = I + sum(Iv_v)
    return I / cola



if __name__ == '__main__':
    rho = range(10,101, 10)
    I_sim_dat = []
    I_the_dat = []
    for rho_i in rho:
        I_sim_dat.append(mean_interference_sim(rho_i, cola=int(1e4)))
        I_the_dat.append(mean_interference_the(rho_i))


    I_sim_dat1 = []
    I_the_dat1 = []
    for rho_i in rho:
        I_sim_dat1.append(mean_interference_sim(rho_i,  cola=int(1e4), epsilon=0.05))
        I_the_dat1.append(mean_interference_the(rho_i, 0.05))

    I_sim_dat2 = []
    I_the_dat2 = []
    for rho_i in rho:
        I_sim_dat2.append(mean_interference_sim(rho_i,  cola=int(1e4), epsilon=0.08))
        I_the_dat2.append(mean_interference_the(rho_i, 0.08))
    Iv_u = 0
    Iu_v = 0

    from tools import save_json_dat, save_pic, read_json_dat
    save_json_dat("rho",rho)
    save_json_dat("I_sim", I_sim_dat)
    save_json_dat("I_the", I_the_dat)

    rho_r = read_json_dat("rho")
    I_sim_r = read_json_dat("I_sim")
    I_the_r = read_json_dat("I_the")

    import matplotlib.pyplot as plt
    import pic_style
    pic_style.xuebao_style()  # 图片格式
    fig = plt.figure()  # 图片绘制
    plt.plot(rho_r, I_the_r)
    plt.scatter(rho_r, I_sim_r)

    plt.plot(rho_r, I_the_dat1)
    plt.scatter(rho_r, I_sim_dat1)

    plt.plot(rho_r, I_the_dat2)
    plt.scatter(rho_r, I_sim_dat2)

    plt.legend([r'理论 $\epsilon=0.1$',r'仿真 $\epsilon=0.1$',
                r'理论 $\epsilon=0.05$',r'仿真 $\epsilon=0.05$',
                r'理论 $\epsilon=0.08$',r'仿真 $\epsilon=0.08$'])
    plt.xlabel(r'车辆密度 $\rho$（辆/米）')
    plt.ylabel('平均干扰功率（W）')

    save_pic(fig, '干扰.svg')
    plt.show()