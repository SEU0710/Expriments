Pt_v = 10e-3  # W
Pt_u = 20e-3

fc_v = 76.5e9  # Hz
fc_u = 78.5e9  # Hz
Gv = 30  # dBi
Gu = 30  # dBi
Bv = 20e6  # Hz
Bu = 20e6  # Hz

lamda_v = 3e8 / fc_v
lamda_u = 3e8 / fc_u

epsilon = 0.1
epsilon_v_u = 0.02
epsilon_u_v = 0.05
dv = 100  # m
du = 250  # m
dw = 3.6  # m
dh = 10  # m

hv = 1  # m
hu = 7  # m

L = 1e3  # m

sigma = 30  # dBsm

theta = 20  # degree
varphi = 10  # degree



# 参数转换
def d2b(a):  # dB to basic unit
    return 10 ** (a / 10)

def d2r(a):  # degree to rad
    return 0.0174532925 * a

