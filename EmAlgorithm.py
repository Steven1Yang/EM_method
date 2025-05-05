import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils.estimationf import em_algorithm

df = pd.read_excel('height.xlsx')
column_data = df.iloc[2:95, 1].values
p_m, p_f, p_x, p_mx, p_fx = [0] * 95, [0] * 95, [0] * 95, [0] * 95, [0] * 95


miu1_new, miu2_new, sigma1_new, sigma2_new, p_new = em_algorithm(column_data)

x = np.linspace(155, 200, 1000)
y = (p_new / (np.sqrt(2 * np.pi * sigma1_new ** 2))) * np.exp(-0.5 * ((x - miu1_new) / sigma1_new) ** 2) \
    + ((1 - p_new) / (np.sqrt(2 * np.pi * sigma2_new ** 2))) * np.exp(-0.5 * ((x - miu2_new) / sigma2_new) ** 2)
x_male = np.linspace(miu1_new - 3 * sigma1_new, miu1_new + 3 * sigma1_new, 100)
y_male = (1 / (np.sqrt(2 * np.pi) * sigma1_new)) * np.exp(-0.5 * ((x_male - miu1_new) / sigma1_new) ** 2)
x_female = np.linspace(miu2_new - 3 * sigma2_new, miu2_new + 3 * sigma2_new, 100)
y_female = (1 / (np.sqrt(2 * np.pi) *sigma2_new))*np.exp(-0.5 * ((x_female - miu2_new) / sigma2_new) ** 2)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
ax1.plot(x_male, 0.8835841461125267*y_male, color='blue', label='Male Height')
ax1.plot(x_female, 0.11641585388747333*y_female, color='red', label='Female Height')
ax1.plot(x, y, color='black', label='Mixture Gaussian',linestyle='--')
ax1.legend()
ax1.set_title("Figure 1: Mixture Gaussian Distribution")
ax1.set_xlabel("Height")
ax1.set_ylabel("Probability Density")
ax1.text(155, 0.06, 'Male Weight: {:.2f}'.format(p_new), color='blue')
ax1.text(155, 0.055, 'Female Weight: {:.2f}'.format(1 - p_new), color='red')

ax2.plot(x_male, y_male, color='blue', label='Male Height')
ax2.plot(x_female, y_female, color='red', label='Female Height')
ax2.legend()
ax2.text(187.25, 0.138, 'Male Weight: {:.2f}'.format(p_new), color='blue')
ax2.text(187.25, 0.123, 'Female Weight: {:.2f}'.format(1 - p_new), color='red')
ax2.text(miu1_new, max(y_male), f"μ1 = {miu1_new:.2f}, σ1 = {sigma1_new:.2f}", ha='center', va='bottom')
ax2.text(miu2_new, max(y_female), f"μ2 = {miu2_new:.2f}, σ2 = {sigma2_new:.2f}", ha='center', va='bottom')
ax2.set_title("Figure 2: Male and Female Height Distribution")
ax2.set_xlabel("Height")
ax2.set_ylabel("Probability Density")
plt.tight_layout()
plt.show()

print('男生身高均值为：', miu1_new, '男生身高标准差为：', sigma1_new, '男生样本数在总样本数所占比例：', p_new)
print('女生身高均值为：', miu2_new, '女生身高标准差为：', sigma2_new, '女生样本数在总样本数所占比例：', 1 - p_new)