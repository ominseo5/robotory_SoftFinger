import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# parameter와 exp-type 접근
parameter = input ('Enter a parameter to show (d, h, t, n) :')
exp_case = input('Enter a exp-type to show (dn, dp, un, up) :')


# 엑셀 파일 로드 (파일 경로를 맞추어야 함)
filename = f'parameter_to_force_{parameter}.xlsx'

# parameter에 따른 trial num / dict와 여러 필요 변수들 선언

index_dict = {
    "d":["18mm", "21mm", "24mm", "27mm", "30mm", "33mm"],
    "h":["9mm", "12mm", "15mm", "18mm", "21mm", "24mm", "27mm"],
    "t":["0.5mm", "0.6mm", "0.7mm", "0.8mm", "0.9mm"],
    "n":['n4','n6','n8','n10','n12']
}

name = {
    "d":"diameter",
    "h":"height",
    "t":"thickness",
    "n":"n-values"
}

unit = {
    'd':'mm',
    'h':'mm',
    't':'mm',
    'n':None
}

index_dict_numonly = {
    "d": [18,21,24,27,30,33],
    "h": [9,12,15,18,21,24,27],
    "t": [0.5,0.6,0.7,0.8,0.9],
    "n": [4, 6, 8, 10, 12]
}

pressures = ["10kpa", "20kpa", "30kpa", "40kpa", "50kpa", "60kpa", "70kpa"],
p_num = ['10', '20', '30', '40', '50', '60', '70']

markers= ['o', 's', 'D', '^', 'v', 'p', '*']
colors= ['red', 'green', 'blue', 'black', 'violet', 'gray', 'orange']

df = pd.read_excel(filename, sheet_name = exp_case)
df.index = index_dict[parameter]
df = df.drop("Unnamed: 0", axis=1)

fig = plt.figure(figsize=(10, 6))

if exp_case == 'dn' or exp_case == 'un':
    num = 5
else:
    num = 7

for i in range(num):
    data = []
    mean = []
    std = []

    for para in index_dict[parameter]:
        force_data = df.loc[para, [f"{10*(i+1)}kpa.1", f"{10*(i+1)}kpa.2", f"{10*(i+1)}kpa.3"]]
        force_mean = np.mean(force_data, axis=0)
        force_std = np.std(force_data, axis=0)
        data.append(list(force_data))
        mean.append(float(round(force_mean, 3)))
        std.append(float(round(force_std, 3)))

    data = np.array(data)
    mean = np.array(mean)
    std = np.array(std)
    # errorbar 그리기
    plt.errorbar(index_dict_numonly[parameter], mean, yerr=std, fmt=f'-{markers[i]}', capsize=5, label=f'{10*(i+1)}kpa', linewidth = 0.5, markersize = 4, ecolor=colors[i], color=colors[i])

plt.xlabel(f'different {parameter}-values ({unit[parameter]})')
plt.ylabel('Force (N)')
plt.title(f'Force-{name[parameter]} Error Bars for {exp_case} case, different {name[parameter]}')
plt.legend()
plt.grid(True)
plt.xticks(index_dict_numonly[parameter])
plt.show()
name_to_save = input('press file name to be saved: ')
fig.savefig(name_to_save)