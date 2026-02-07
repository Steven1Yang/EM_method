import os
from Data_handler import load_data, plot_results
from Em_engine import em_algorithm


def start_analysis(file_name):
    # 检查文件是否存在，防止程序崩溃
    if not os.path.exists(file_name):
        print(f"错误：找不到文件 '{file_name}'，请检查文件名或路径是否正确。")
        return

    print(f"--- 正在处理文件: {file_name} ---")

    try:
        # 1. 调用 data_handler 加载数据
        height_data = load_data(file_name)

        # 2. 调用 em_engine 执行核心算法
        # 返回：男生均值, 女生均值, 男生标准差, 女生标准差, 男生比例
        results = em_algorithm(height_data)
        mu1, mu2, s1, s2, p = results

        # 3. 打印终端结果
        print("\n" + "=" * 40)
        print(f"【男生估计结果】")
        print(f"均值: {mu1:.2f} cm | 标准差: {s1:.2f} | 样本占比: {p:.2%}")
        print("-" * 40)
        print(f"【女生估计结果】")
        print(f"均值: {mu2:.2f} cm | 标准差: {s2:.2f} | 样本占比: {1 - p:.2%}")
        print("=" * 40 + "\n")

        # 4. 调用 data_handler 绘制可视化图表
        plot_results(height_data, results)

    except Exception as e:
        print(f"程序执行时发生错误: {e}")


if __name__ == "__main__":
    # --- 你只需要在这里修改你的 Excel 文件名 ---
    target_file = 'height.xlsx'
    start_analysis(target_file)