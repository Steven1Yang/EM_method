import numpy as np


def e_step(data, mu1, sigma1, mu2, sigma2, p):
    # 计算第一个分布（男）的概率密度
    pdf1 = (1 / (np.sqrt(2 * np.pi) * sigma1)) * np.exp(-0.5 * ((data - mu1) / sigma1) ** 2)
    # 计算第二个分布（女）的概率密度
    pdf2 = (1 / (np.sqrt(2 * np.pi) * sigma2)) * np.exp(-0.5 * ((data - mu2) / sigma2) ** 2)

    # 计算加权后的概率（分子）
    weighted1 = pdf1 * p
    weighted2 = pdf2 * (1 - p)

    # 归一化，得到每个点属于该分布的权重（后验概率）
    sum_pdf = weighted1 + weighted2
    gamma1 = weighted1 / sum_pdf
    gamma2 = weighted2 / sum_pdf

    return gamma1, gamma2


def m_step(data, gamma1, gamma2):
    # 获取样本总数
    n = len(data)
    # 计算权重的总和
    sum_g1 = np.sum(gamma1)
    sum_g2 = np.sum(gamma2)

    # 更新均值 mu (加权平均)
    new_mu1 = np.sum(gamma1 * data) / sum_g1
    new_mu2 = np.sum(gamma2 * data) / sum_g2

    # 更新标准差 sigma
    new_sigma1 = np.sqrt(np.sum(gamma1 * (data - new_mu1) ** 2) / sum_g1)
    new_sigma2 = np.sqrt(np.sum(gamma2 * (data - new_mu2) ** 2) / sum_g2)

    # 更新混合系数 p
    new_p = sum_g1 / n

    return new_mu1, new_mu2, new_sigma1, new_sigma2, new_p


def em_algorithm(data, max_iter=100, tol=1e-6):
    # 初始参数设定
    mu1, mu2 = 175.0, 165.0
    sigma1, sigma2 = 5.0, 5.0
    p = 0.5

    # 迭代循环
    for i in range(max_iter):
        # 记录旧参数
        old_params = np.array([mu1, mu2, p])

        # E步
        g1, g2 = e_step(data, mu1, sigma1, mu2, sigma2, p)
        # M步
        mu1, mu2, sigma1, sigma2, p = m_step(data, g1, g2)

        # 检查收敛
        new_params = np.array([mu1, mu2, p])
        if np.linalg.norm(new_params - old_params) < tol:
            print(f"Algorithm converged at iteration {i + 1}")
            break

    return mu1, mu2, sigma1, sigma2, p