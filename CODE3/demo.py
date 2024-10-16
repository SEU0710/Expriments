
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
        if (v_x**2 > (vertical_spacing / np.tan(horizontal_angle / 2)) ** 2
                     + (hight_intercept / np.tan(vertical_angle / 2) ** 2)):
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


# def radar_theory_interference():



if __name__ == '__main__':
    import numpy as np
    m = 10000
    I_ = []
    I_the_dat = []
    rho = np.arange(10,100,10)
    for rho_i in rho:
        I = 0
        for k in range(m):
            v_x = vehicle_distribution(rho_i, 1e3, 10, 0.1)
            v_d = facing_vehicle_distance(v_x, 3.6, 20)
            Iv_v = radar_recv_power(v_d, 10e-3, coe=(1000 * 0.004 / (4 * np.pi)) ** 2)
            I = I + sum(Iv_v)
        I_.append(I / m)

        rho_h = (1 - np.exp(-2 * 0.1 * rho_i / 1e3 * 10)) / (2 * 10)
        varepsilon = (1000 * 0.004 / (4 * np.pi)) ** 2
        # I_the = varepsilon * rho_h * 10e-3 * np.tan(20 / 2) / 3.6
        I_the = varepsilon * rho_h * 10e-3 * (np.pi / 2 - np.arctan(1/np.tan(20 / 2))) / 3.6
        I_the_dat.append(I_the)
    Iv_u = 0
    Iu_v = 0


    import matplotlib.pyplot as plt
    from style import savePic
    fig = plt.figure()
    plt.scatter(rho, I_)
    plt.plot(rho, I_the_dat)
    # plt.scatter(I_, np.zeros(np.size(I_)))

    savePic(fig, '干扰.svg')
    plt.show()