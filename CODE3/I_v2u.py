import numpy as np

from demo import *

def mean_interference_the_v2u(rho_i, epsilon_vu=0.02):
    rho_h = (1 - np.exp(-2 * 1 * rho_i / L * dh)) / (2 * dh)
    varepsilon = d2b(Gv) * d2b(Gu) * (lamda_u / (4 * np.pi)) ** 2
    delta = np.sqrt((dw / 2 / np.tan(d2r(theta) / 2)) ** 2 + ((hu-hv) / np.tan(d2r(varphi) / 2))**2)
    I_the = varepsilon * rho_h * Pt_u / delta  # 近似
    # I_the = (varepsilon * rho_h * Pt_u * (np.pi / 2 - np.arctan(delta / np.sqrt((dw/2)**2 + (hu-hv)**2)))
    #          / np.sqrt((dw/2)**2 + (hu-hv)**2))  # 非近似
    return epsilon_vu * I_the

def mean_interference_sim_v2u(rho_i, cola:int, epsilon_vu=0.02):
    I = 0
    for i in range(cola):  # 蒙特卡洛次数
        v_x = vehicle_distribution(rho_i, L, dh, 1)
        v_d = vehicle_rsu_distance(v_x, dw/2, hu-hv, d2r(theta), d2r(varphi))
        Iv_u = radar_recv_power(v_d, Pt_u, coe=d2b(Gv) * d2b(Gu) * (lamda_u / (4 * np.pi)) ** 2)
        I = I + sum(Iv_u)
    return epsilon_vu * (I / cola)



if __name__ == '__main__':
    rho = range(10,101, 10)
    I_sim_dat = []
    I_the_dat = []
    for rho_i in rho:
        I_sim_dat.append(mean_interference_sim_v2u(rho_i, cola=int(1e3)))
        I_the_dat.append(mean_interference_the_v2u(rho_i))


    I_sim_dat1 = []
    I_the_dat1 = []
    for rho_i in rho:
        I_sim_dat1.append(mean_interference_sim_v2u(rho_i,  cola=int(1e3), epsilon_vu = 0.015))
        I_the_dat1.append(mean_interference_the_v2u(rho_i, 0.015))

    I_sim_dat2 = []
    I_the_dat2 = []
    for rho_i in rho:
        I_sim_dat2.append(mean_interference_sim_v2u(rho_i,  cola=int(1e3), epsilon_vu = 0.01))
        I_the_dat2.append(mean_interference_the_v2u(rho_i, 0.01))


    from tools import save_json_dat, save_pic, read_json_dat
    save_json_dat("rho",rho)
    save_json_dat("I_sim_v2u", I_sim_dat)
    save_json_dat("I_the_v2u", I_the_dat)

    rho_r = read_json_dat("rho")
    I_sim_r = read_json_dat("I_sim_v2u")
    I_the_r = read_json_dat("I_the_v2u")

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

    plt.legend([r'理论 $\epsilon_{v,u}=0.02$',r'仿真 $\epsilon_{v,u}=0.02$',
                r'理论 $\epsilon_{v,u}=0.015$',r'仿真 $\epsilon_{v,u}=0.015$',
                r'理论 $\epsilon_{v,u}=0.01$',r'仿真 $\epsilon_{v,u}=0.01$'])
    plt.xlabel(r'车辆密度 $\rho$（辆/米）')
    plt.ylabel('平均干扰功率（W）')

    save_pic(fig, '干扰v2u.svg')
    plt.show()