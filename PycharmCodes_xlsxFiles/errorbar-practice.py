import numpy as np
import matplotlib.pyplot as plt

# 샘플 데이터 생성 (리니어한 압력 변위 데이터를 임의로 생성)
displacement = np.linspace(0, 10, 20)  # 변위 데이터 (0에서 10까지 20개 지점)
true_pressure = 10 * displacement + 5  # 리니어한 관계를 가지는 압력 데이터

# 각 지점에서 압력값에 작은 노이즈를 추가하여 3개의 샘플 데이터 생성
np.random.seed(0)  # 재현성을 위해 시드 설정
pressure_samples = np.array([true_pressure + np.random.normal(0, 2, 20) for _ in range(3)]).T

# 각 포인트의 평균과 표준편차 계산
pressure_mean = np.mean(pressure_samples, axis=1)
pressure_std = np.std(pressure_samples, axis=1)

print(pressure_samples)
print(pressure_mean)
print(pressure_std)
# 그래프 그리기 및 저장
fig = plt.figure(figsize=(6, 12))
plt.errorbar(displacement, pressure_mean, yerr=pressure_std, fmt='-o', ecolor='blue', color='blue', capsize=5, label='Pressure vs Displacement')
plt.xlabel('Displacement')
plt.ylabel('Pressure')
plt.title('Pressure vs Displacement with Error Bars')
plt.legend()
plt.grid(True)
plt.show()