import json
def save_json_dat(name, value):
    new_data = {name: list(value)}
    with open(r'./dat/data.json', 'r') as fr:
        data = json.load(fr)
        data.update(new_data)
    with open(r'./dat/data.json', 'w') as fw:
        json.dump(data, fw, ensure_ascii=False, indent=4)

def read_json_dat(name):
    with open(r'./dat/data.json', 'r') as fr:
        data = json.load(fr)
        return data[name]

def save_pic(figure, fname):
    # figure.set_figwidth(6*cm2inch)
    # figure.set_figheight(5*cm2inch)
    figure.savefig(rf"./pic/{fname}", dpi=600)
    print(f"图片{fname}已保存！")