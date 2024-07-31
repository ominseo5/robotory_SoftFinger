import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 엑셀 파일 경로 지정
file_path = 'FingerForce_data_table.csv100'

# 데이터 종류 라벨링 (dn, dp, un, up) 4 cases
typedn = ['Weight_dn9mm', 'Weight_dn12mm', 'Weight_dn15mm', 'Weight_dn18mm', 'Weight_dn21mm', 'Weight_dn24mm', 'Weight_dn27mm']
typedp = ['Weight_dp9mm', 'Weight_dp12mm', 'Weight_dp15mm', 'Weight_dp18mm', 'Weight_dp21mm', 'Weight_dp24mm', 'Weight_dp27mm']
typeun = ['Weight_un9mm', 'Weight_un12mm', 'Weight_un15mm', 'Weight_un18mm', 'Weight_un21mm', 'Weight_un24mm', 'Weight_un27mm']
typeup = ['Weight_up9mm', 'Weight_up12mm', 'Weight_up15mm', 'Weight_up18mm', 'Weight_up21mm', 'Weight_up24mm', 'Weight_up27mm']
    
# 엑셀 파일을 읽어 데이터프레임으로 로드
df = pd.read_csv(file_path)

# Define markers and colors for better distinction
markers= ['o', 's', 'D', '^', 'v', 'p','*']
colors= ['red', 'green', 'blue', 'black', 'gray', 'violet', 'orange']
kpa_index= [10, 20, 30, 40, 50, 60, 70]

# Update the DataFrame with the correct index
df.index = kpa_index

# Combined 'dn' series
fig = plt.figure(figsize=(6, 12))

for i, column in enumerate(typedn):
    plt.plot(df.index, df[column], label=column, marker=markers[i], color=colors[i])

plt.title('Weights Over Pressure (dn series: 9mm, 12mm, 15mm, 18mm, 21mm, 24mm, 27mm)')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Weight (N)')
plt.legend(loc='upper left')
plt.grid(True)
fig.savefig('dn_series.png')

# Combined 'dp' series
fig = plt.figure(figsize=(6, 12))

for i, column in enumerate(typedp):
    plt.plot(df.index, df[column], label=column, marker=markers[i], color=colors[i])

plt.title('Weights Over Pressure (dp series: 9mm, 12mm, 15mm, 18mm, 21mm, 24mm, 27mm)')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Weight (N)')
plt.legend(loc='upper left')
plt.grid(True)
fig.savefig('dp_series.png')

# Combined 'un' series
fig = plt.figure(figsize=(6, 12))

for i, column in enumerate(typeun):
    plt.plot(df.index, df[column], label=column, marker=markers[i], color=colors[i])

plt.title('Weights Over Pressure (un series: 9mm, 12mm, 15mm, 18mm, 21mm, 24mm, 27mm)')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Weight (N)')
plt.legend(loc='upper left')
plt.grid(True)
fig.savefig('un_series.png')

# Combined 'up' series
fig = plt.figure(figsize=(6, 12))

for i, column in enumerate(typeup):
    plt.plot(df.index, df[column], label=column, marker=markers[i], color=colors[i])

plt.title('Weights Over Pressure (up series: 9mm, 12mm, 15mm, 18mm, 21mm, 24mm, 27mm)')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Weight (N)')
plt.legend(loc='upper left')
plt.grid(True)
fig.savefig('up_series.png')

# Create subplots for 'dn' series
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 20))

for i, column in enumerate(typedn):
    ax = axes[i // 2, i % 2]
    ax.plot(df[column], label=column, marker=markers[i], color=colors[i])
    ax.set_title(column)
    ax.set_xlabel('Pressure (kPa)')
    ax.set_ylabel('Weight (N)')
    ax.legend()
    ax.grid(True)

fig.suptitle('Weights Over Pressure (dn series)')
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout rect to make room for the title
plt.subplots_adjust(hspace=0.7, wspace=0.2)  # Adjust horizontal and vertical space
fig.savefig('dn_series_indiv.png')

# Create subplots for 'dp' series
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 20))

for i, column in enumerate(typedp):
    ax = axes[i // 2, i % 2]
    ax.plot(df[column], label=column, marker=markers[i], color=colors[i])
    ax.set_title(column)
    ax.set_xlabel('Pressure (kPa)')
    ax.set_ylabel('Weight (N)')
    ax.legend()
    ax.grid(True)

fig.suptitle('Weights Over Pressure (dp series)')
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout rect to make room for the title
plt.subplots_adjust(hspace=0.7, wspace=0.2)  # Adjust horizontal and vertical space
fig.savefig('dp_series_indiv.png')

# Create subplots for 'un' series
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 20))

for i, column in enumerate(typeun):
    ax = axes[i // 2, i % 2]
    ax.plot(df[column], label=column, marker=markers[i], color=colors[i])
    ax.set_title(column)
    ax.set_xlabel('Pressure (kPa)')
    ax.set_ylabel('Weight (N)')
    ax.legend()
    ax.grid(True)

fig.suptitle('Weights Over Pressure (un series)')
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout rect to make room for the title
plt.subplots_adjust(hspace=0.7, wspace=0.2)  # Adjust horizontal and vertical space
fig.savefig('un_series_indiv.png')

# Create subplots for 'up' series
fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(10, 20))

for i, column in enumerate(typeup):
    ax = axes[i // 2, i % 2]
    ax.plot(df[column], label=column, marker=markers[i], color=colors[i])
    ax.set_title(column)
    ax.set_xlabel('Pressure (kPa)')
    ax.set_ylabel('Weight (N)')
    ax.legend()
    ax.grid(True)

fig.suptitle('Weights Over Pressure (up series)')
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout rect to make room for the title
plt.subplots_adjust(hspace=0.7, wspace=0.2)  # Adjust horizontal and vertical space
fig.savefig('up_series_indiv.png')