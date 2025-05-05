import numpy as np
def e_step(column_data, miu1, sigma1, miu2, sigma2, p):
    p_m = (1 / ((np.sqrt(2 * np.pi)) * sigma1)) * np.exp(-0.5 * (column_data - miu1) ** 2 / (sigma1 ** 2)) * p
    p_f = (1 / ((np.sqrt(2 * np.pi)) * sigma2)) * np.exp(-0.5 * (column_data - miu2) ** 2 / (sigma2 ** 2)) * (1 - p)
    p_x = p_m + p_f
    p_mx = p_m / p_x
    p_fx = p_f / p_x
    return p_mx, p_fx, p_x, p_m, p_f

def m_step(column_data, p_mx, p_fx):
    sum_p_mx = np.sum(p_mx)
    sum_p_fx = np.sum(p_fx)
    numerator_m = np.sum(p_mx * column_data)
    numerator_f = np.sum(p_fx * column_data)
    miu1_new = numerator_m / sum_p_mx
    miu2_new = numerator_f / sum_p_fx
    numerator_ms = np.sum(p_mx * ((column_data - miu1_new) ** 2))
    numerator_fs = np.sum(p_fx * ((column_data - miu2_new) ** 2))
    sigma1_new = np.sqrt(numerator_ms / sum_p_mx)
    sigma2_new = np.sqrt(numerator_fs / sum_p_fx)
    p_new = sum_p_mx / len(column_data)
    return miu1_new, miu2_new, sigma1_new, sigma2_new, p_new

def em_algorithm(column_data):
    miu1, miu2, sigma1, sigma2, p = 175, 165, 5, 5, 0.5
    f_log = -10000
    for i in range(100):
        p_mx, p_fx, p_x, p_m, p_f = e_step(column_data, miu1, sigma1, miu2, sigma2, p)
        miu1, miu2, sigma1, sigma2, p = m_step(column_data, p_mx, p_fx)
        new_f_log = np.sum(np.log(p * p_m) + np.log((1 - p) * p_f))
        if abs(new_f_log - f_log) < 1e-10:
            break
        f_log = new_f_log
    return miu1, miu2, sigma1, sigma2, p