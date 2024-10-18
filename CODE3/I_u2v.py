from demo import *

def mean_interference_the_u2v(delta_l=50, epsilon_uv=0.05):
    varepsilon = d2b(Gv) * d2b(Gu) * (lamda_v / (4 * np.pi)) ** 2
    I_the = varepsilon * epsilon_uv * Pt_u /(du*(du-delta_l))
    return I_the

def mean_interference_sim_u2v(delta_l, epsilon_uv=0.05):
    varepsilon = d2b(Gv) * d2b(Gu) * (lamda_v / (4 * np.pi)) ** 2
    # I_the = varepsilon * epsilon_uv * Pt_u / ((du-delta_l)**2 + dw**2 + (hu-hv)**2)
    I_the = varepsilon * epsilon_uv * Pt_u / ((du - delta_l) ** 2)
    return I_the

if __name__ == '__main__':
    delta = range(20,60, 5)
    I_sim_dat = []
    I_the_dat = []
    for l in delta:
        I_the_dat.append(mean_interference_the_u2v(delta_l=l))
        I_sim_dat.append(mean_interference_sim_u2v(delta_l=l))

    I_sim_dat1 = []
    I_the_dat1 = []
    for l in delta:
        I_the_dat1.append(mean_interference_the_u2v(delta_l=l, epsilon_uv=0.03))
        I_sim_dat1.append(mean_interference_sim_u2v(delta_l=l, epsilon_uv=0.03))

    I_sim_dat2 = []
    I_the_dat2 = []
    for l in delta:
        I_the_dat2.append(mean_interference_the_u2v(delta_l=l, epsilon_uv=0.01))
        I_sim_dat2.append(mean_interference_sim_u2v(delta_l=l, epsilon_uv=0.01))


    from tools import save_json_dat, save_pic, read_json_dat
    save_json_dat("delta",delta)
    save_json_dat("I_sim_u2v", I_sim_dat)
    save_json_dat("I_the_u2v", I_the_dat)

    delta_r = read_json_dat("delta")
    I_sim_r = read_json_dat("I_sim_u2v")
    I_the_r = read_json_dat("I_the_u2v")

    import matplotlib.pyplot as plt
    import pic_style
    pic_style.xuebao_style()  # 图片格式
    fig = plt.figure()  # 图片绘制
    plt.plot(delta_r, I_sim_r, linestyle=':')
    plt.plot(delta_r, I_the_r)
    plt.scatter(delta_r, I_the_r)

    plt.plot(delta_r, I_sim_dat1, linestyle=':')
    plt.plot(delta_r, I_the_dat1)
    plt.scatter(delta_r, I_the_dat1)

    plt.plot(delta_r, I_sim_dat2, linestyle=':')
    plt.plot(delta_r, I_the_dat2)
    plt.scatter(delta_r, I_the_dat2)

    plt.legend([r'最大 $\epsilon_{u,v}=0.05$', r'理论 $\epsilon_{u,v}=0.05$', r'仿真 $\epsilon_{u,v}=0.05$',
                r'最大 $\epsilon_{u,v}=0.03$', r'理论 $\epsilon_{u,v}=0.03$', r'仿真 $\epsilon_{u,v}=0.03$',
                r'最大 $\epsilon_{u,v}=0.01$', r'理论 $\epsilon_{u,v}=0.01$', r'仿真 $\epsilon_{u,v}=0.01$'], ncol=2, frameon=False)
    plt.xlabel(r'覆盖路段长 $l$（m）')
    plt.ylabel('平均干扰功率（W）')
    plt.ylim([1e-9, 1.85e-8])

    save_pic(fig, '干扰u2v.svg')
    plt.show()