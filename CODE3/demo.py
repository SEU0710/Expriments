from params import *
import numpy as np

def vehicle_distribution(rho_initial,  road_len, core_distance, epsilon=1.0)->list:
    """
    在长度为road_len的路段上，车辆服从密度为rho_initial硬核距离为core_distance
    的HMCP过程, epsilon为概率因子； 返回车辆在该路段上所处位置的水平坐标。
    """
    rho = epsilon * rho_initial
    v_num = np.random.poisson(rho)
    v_coor = np.random.rand(v_num) * road_len  # mark
    v_sort = np.sort(v_coor)
    v_mhcp = []
    i, j = 0, 0
    try:
        v_mhcp.append(v_sort[0])
        while i < v_num:  # select
            if v_sort[i] - v_sort[j] >= core_distance:
                v_mhcp.append(v_sort[i])
                j = i
            i += 1
    except IndexError:
        pass

    return v_mhcp


def facing_vehicle_distance(vehicle_location, vertical_spacing, horizontal_angle)->list:
    """
    被干扰车辆与在雷达水平视角内的干扰车辆之间的视线距离
    """
    v_distance = []
    for v_x in vehicle_location:
        if v_x > vertical_spacing / np.tan(horizontal_angle / 2):
            v_distance.append((v_x ** 2 + vertical_spacing ** 2) ** 0.5)

    return v_distance


def vehicle_rsu_distance(vehicle_location, vertical_spacing, hight_intercept, horizontal_angle, vertical_angle)->list:
    """
    路侧单元与在汽车雷达视场内的干扰车辆之间的视线距离
    """
    u_distance = []
    for v_x in vehicle_location:
        if (v_x >= ((vertical_spacing / np.tan(horizontal_angle / 2)) ** 2
                     + (hight_intercept / np.tan(vertical_angle / 2) ** 2)) ** 0.5):
            u_distance.append((v_x ** 2 + vertical_spacing ** 2 + hight_intercept ** 2) ** 0.5)

    return u_distance



def radar_recv_power(radar_distance, power_trans, path_exponent=-2, **kwargs)->list:
    """
    由雷达方程得到接收功率；
    接收功率与传播路径关系由path_exponent描述，一般取-2或-4.
    """
    factor = 1
    if kwargs:
        for val in kwargs.values():
            factor = val * factor

    return [factor * power_trans * dist ** path_exponent
            for dist in radar_distance]


if __name__ == '__main__':
    from params import *
    import numpy as np

    rho = range(10,101, 10)
    I_sim_dat = []
    I_the_dat = []
    for rho_i in rho:
        I_sim_dat.append(mean_interference_sim(rho_i, cola=int(1e4)))
        I_the_dat.append(mean_interference_the(rho_i))


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

    plt.legend([r'理论 $\epsilon=0.1$',r'仿真 $\epsilon=0.1$'])
    plt.xlabel(r'车辆密度 $\rho$（辆/米）')
    plt.ylabel('平均干扰功率（W）')

    # save_pic(fig, '干扰.svg')
    plt.show()