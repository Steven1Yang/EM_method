# 📊 EM Algorithm: Gaussian Mixture Modeling for Height Data

This project implements the **Expectation-Maximization (EM)** algorithm to estimate parameters of a **Gaussian Mixture Model (GMM)** applied to height data. The goal is to model the height distribution as a mixture of two normal distributions, typically representing male and female groups.

## 📁 Project Structure

```

EMAlgorithm/
├── Data_handler.py             # Main script to run the EM algorithm and plot results
├── Em_engine.py             # Main script to run the EM algorithm and plot results
├── EmAlgorithm.py             # Main script to run the EM algorithm and plot results
├── height.xlsx                # Input dataset (height values)
└── README.md                  # Project documentation

````

## 📦 Dependencies

Make sure you have the following Python libraries installed:

```bash
pip install numpy pandas matplotlib openpyxl
````

> `openpyxl` is required for reading `.xlsx` Excel files.

## 🚀 How to Run

1. Place your height data in the `height.xlsx` file.
2. Execute the script:

```bash
python EmAlgorithm.py
```

This will:

* Load the data from Excel,
* Run the EM algorithm to estimate GMM parameters,
* Plot the overall mixture and individual distributions,
* Print the mean, standard deviation, and weight for each Gaussian component.

## 📈 Output

The script produces two plots:

* **Mixture Gaussian Distribution** – Shows the combined GMM and individual distributions.
* **Separate Components** – Displays each Gaussian component with labels and statistics.

It also prints:

```text
Male mean height: 174.22, standard deviation: 4.51, proportion: 0.88
Female mean height: 162.40, standard deviation: 3.89, proportion: 0.12
```

## 📊 Dataset

* File: `height.xlsx`
* Data Range: rows 3 to 95, column 2 (zero-indexed)
* Assumption: the dataset is a mixture of two Gaussian distributions.

## 🧠 EM Algorithm Overview

The Expectation-Maximization algorithm iteratively estimates the parameters of a mixture model:

1. **Initialization**: Start with initial guesses for means, variances, and mixing weights.
2. **E-Step**: Estimate the probability that each data point belongs to each distribution.
3. **M-Step**: Update the parameters to maximize the expected log-likelihood.
4. **Repeat** until convergence.

## 💡 Use Cases

* Unsupervised clustering with continuous data
* Modeling population subgroups in statistics
* Educational demonstration of the EM algorithm

---

Feel free to open issues or contribute if you'd like to improve the code or add more features!
