import matplotlib.pyplot as plt

def xuebao_style():
    cm2inch = 0.3937
    #cm2inch = 0.380
    plt.rcParams['figure.figsize'] = (10*cm2inch, 8*cm2inch)
    # plt.rcParams['figure.figsize'] = (12*cm2inch, 10*cm2inch)
    plt.rcParams['font.family'] = ['SimSun', 'Times New Roman']
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['mathtext.fontset'] = 'stix'
    # plt.rcParams['mathtext.it'] = 'ok'
    plt.rcParams['font.size'] = 8
    plt.rcParams['lines.linewidth'] = 0.5  # 要求0.5
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['axes.linewidth'] = 0.5
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    # plt.rcParams['xtick.bottom'] = False
    # plt.rcParams['ytick.left'] = False
    plt.rcParams['axes.labelpad'] = 5
    # plt.rcParams['ytick.major.pad'] = 3
    # plt.rcParams['xtick.major.pad'] = 3
    plt.rcParams['ytick.major.pad'] = 3
    plt.rcParams['xtick.major.pad'] = 3
    #plt.rcParams['savefig.dpi'] = 600
    plt.rcParams['savefig.format'] = 'png'
    plt.rcParams['ytick.major.width'] = 0.5
    plt.rcParams['xtick.major.width'] = 0.5
    # plt.rcParams['figure.subplot.bottom'] = 0.15
    # plt.rcParams['figure.subplot.top'] = 0.95
    # plt.rcParams['figure.subplot.left'] = 0.15
    # plt.rcParams['figure.subplot.right'] = 0.95
    # plt.rcParams['grid.linewidth'] = 0.5
    # plt.rcParams['grid.linestyle'] = ':'
    # plt.rcParams['grid.color'] = 'gray'
    # plt.rcParams['axes.size'] = (4, 3)
    #print(plt.rcParams.keys())

if __name__ == '__main__':
    xuebao_style()
