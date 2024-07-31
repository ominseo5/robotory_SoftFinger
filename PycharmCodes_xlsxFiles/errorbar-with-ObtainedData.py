import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 엑셀 파일 로드 (파일 경로를 맞추어야 함)
filename = 'data_return_0726.xlsx'

markers= ['o', 's', 'D', '^', 'v', 'p','*']
colors= ['red', 'green', 'blue', 'black', 'gray', 'violet', 'orange']

# 특정 케이스에 대한 데이터 추출
# d_case = input("Enter a finger-size to show (9, 12, 15, 18, 21, 24, 27): ")
#
# # 데이터 로드 from xlsx, 단일 사이즈에 대해서 보고싶을 경우
# df = pd.read_excel(filename, sheet_name=f'{d_case}mm') #sheetname : 9mm, 12mm, 15mm, 18mm, 21mm, 24mm, 27mm
# case_prefix = [f"Weight_dn{d_case}", f"Weight_dp{d_case}", f"Weight_un{d_case}", f"Weight_up{d_case}"]
#
# df = pd.read_excel(filename, sheet_name = f'{d_case}mm')
# pressures = ["10kpa", "20kpa", "30kpa", "40kpa", "50kpa", "60kpa", "70kpa"]
# df.index = pressures
# df = df.drop("Unnamed: 0", axis=1)
#
# # 압력 단계별 데이터 추출 및 그래프 그리기
# fig = plt.figure(figsize=(10, 6))
#
# # 단일 fingersize 보고싶을 때
# for i in range(4):
#     data = []
#     mean = []
#     std = []
#
#     for pressure in pressures:
#         pressure_data = df.loc[pressure, [f"{case_prefix[i]}.1", f"{case_prefix[i]}.2", f"{case_prefix[i]}.3"]]
#         pressure_mean = np.mean(pressure_data, axis=0)
#         pressure_std = np.std(pressure_data, axis=0)
#         data.append(list(pressure_data))
#         mean.append(float(round(pressure_mean, 3)))
#         std.append(float(round(pressure_std, 3)))
#
#     data = np.array(data)
#     mean = np.array(mean)
#     std = np.array(std)
#
#     # errorbar 그리기
#     plt.errorbar(pressures, mean, yerr=std, fmt='-o', capsize=5, label=f'{case_prefix[i]}_series')
#
# plt.xlabel('Pressure')
# plt.ylabel('Force')
# plt.title(f'Force-Pressure with Error Bars for {d_case}mm')
# plt.legend()
# plt.grid(True)
# plt.show()
#fig.savefig(f'{d_case}mm_force_pressure_errorbar.png')

## exp_type 따라 보고싶을 때
exp_case = input('Enter a exp-type to show (dn, dp, un, up dn_new, un_new) :')

df = pd.read_excel(filename, sheet_name = exp_case)
pressures = ["10kpa", "20kpa", "30kpa", "40kpa", "50kpa", "60kpa", "70kpa"]
p_num = ['10', '20', '30', '40', '50', '60', '70']
df.index = pressures
df = df.drop("Unnamed: 0", axis=1)

fig = plt.figure(figsize=(10, 6))

for i in range(7):
    data = []
    mean = []
    std = []

    for pressure in pressures:
        pressure_data = df.loc[pressure, [f"Weight_{exp_case}{3*(i+1)+6}.1", f"Weight_{exp_case}{3*(i+1)+6}.2", f"Weight_{exp_case}{3*(i+1)+6}.3"]]
        pressure_mean = np.mean(pressure_data, axis=0)
        pressure_std = np.std(pressure_data, axis=0)
        data.append(list(pressure_data))
        mean.append(float(round(pressure_mean, 3)))
        std.append(float(round(pressure_std, 3)))

    data = np.array(data)
    mean = np.array(mean)
    std = np.array(std)

    # errorbar 그리기
    plt.errorbar(p_num, mean, yerr=std, fmt=f'-{markers[i]}', capsize=5, label=f'{3*(i+1)+6}mm', linewidth = 0.5, markersize = 4, ecolor=colors[i], color=colors[i])

plt.xlabel('Pressure (kPa)')
plt.ylabel('Force (N)')
plt.title(f'Force-Pressure Error Bars for {exp_case}')
plt.legend()
plt.grid(True)
#plt.show()
name_to_save = input('press file name to be saved: ')
fig.savefig(name_to_save)