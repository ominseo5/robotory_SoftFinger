import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 엑셀 파일 로드 (파일 경로를 맞추어야 함)
filename = 'var_thick_data18mm.xlsx'

markers= ['o', 's', 'D', '^', 'v']
colors= ['red', 'green', 'blue', 'black', 'violet']

## exp_type 따라 보고싶을 때
exp_case = input('Enter a exp-type to show (dn, dp, un, up) :')

df = pd.read_excel(filename, sheet_name = exp_case)
pressures = ["10kpa", "20kpa", "30kpa", "40kpa", "50kpa", "60kpa", "70kpa"]
p_num = ['10', '20', '30', '40', '50', '60', '70']
df.index = pressures
df = df.drop("Unnamed: 0", axis=1)

fig = plt.figure(figsize=(10, 6))

for i in range(5):
    data = []
    mean = []
    std = []
    # 5mm 재실험
    # if i == 0:
    #     i+=1
    for pressure in pressures:
        pressure_data = df.loc[pressure, [f"Weight_{exp_case}180{i+5}.1", f"Weight_{exp_case}180{i+5}.2", f"Weight_{exp_case}180{i+5}.3"]]
        pressure_mean = np.mean(pressure_data, axis=0)
        pressure_std = np.std(pressure_data, axis=0)
        data.append(list(pressure_data))
        mean.append(float(round(pressure_mean, 3)))
        std.append(float(round(pressure_std, 3)))

    data = np.array(data)
    mean = np.array(mean)
    std = np.array(std)

    # errorbar 그리기
    plt.errorbar(p_num, mean, yerr=std, fmt=f'-{markers[i]}', capsize=5, label=f'0.{i+5}mm', linewidth = 0.5, markersize = 4, ecolor=colors[i], color=colors[i])

plt.xlabel('Pressure (kPa)')
plt.ylabel('Force (N)')
plt.title(f'Force-Pressure Error Bars for {exp_case}, different thickness')
plt.legend()
plt.grid(True)
plt.show()
# name_to_save = input('press file name to be saved: ')
# fig.savefig(name_to_save)