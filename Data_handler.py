import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(file_path):
    # 使用 pandas 读取 excel
    df = pd.read_excel(file_path)
    # 根据你的要求：读取第2行到95行，第2列的数据
    # .values 转换为 numpy 数组，.astype(float) 确保是数值类型
    data = df.iloc[2:95, 1].values.astype(float)
    return data


def plot_results(data, params):
    mu1, mu2, s1, s2, p = params

    # 生成 x 轴坐标点，范围覆盖数据最小值到最大值
    x = np.linspace(min(data) - 5, max(data) + 5, 1000)

    # 计算两个高斯分量的密度曲线
    # 男性分量曲线 (乘以权重 p)
    y1 = (p / (np.sqrt(2 * np.pi) * s1)) * np.exp(-0.5 * ((x - mu1) / s1) ** 2)
    # 女性分量曲线 (乘以权重 1-p)
    y2 = ((1 - p) / (np.sqrt(2 * np.pi) * s2)) * np.exp(-0.5 * ((x - mu2) / s2) ** 2)

    # 创建画布
    plt.figure(figsize=(10, 6))

    # 绘制原始数据的直方图
    plt.hist(data, bins=15, density=True, alpha=0.3, color='gray', label='Original Data')

    # 绘制男生曲线
    plt.plot(x, y1, 'b-', lw=2, label=f'Male (mu={mu1:.2f})')
    # 绘制女生曲线
    plt.plot(x, y2, 'r-', lw=2, label=f'Female (mu={mu2:.2f})')
    # 绘制混合后的总曲线
    plt.plot(x, y1 + y2, 'k--', lw=1.5, label='Mixture Gaussian')

    # 图表装饰
    plt.title("Height Distribution - GMM Estimation")
    plt.xlabel("Height (cm)")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)

    # 显示图像
    plt.show()