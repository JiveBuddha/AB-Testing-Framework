import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_ab_histogram(data, group_col, metric_col):
    """
    Plots a histogram of the metric for the two groups.

    :param data: pd.DataFrame - DataFrame containing the test data
    :param group_col: str - Column representing the group
    :param metric_col: str - Column representing the metric
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data, x=metric_col, hue=group_col, kde=True)
    plt.title('Distribution of Metric by Group')
    plt.show()

def plot_confidence_interval(lower, upper):
    """
    Visualizes the confidence interval for the difference in means between two groups.

    :param lower: float - Lower bound of the confidence interval
    :param upper: float - Upper bound of the confidence interval
    """
    plt.figure(figsize=(6, 4))
    plt.errorbar(x=0, y=0, xerr=[[abs(lower)], [upper]], fmt='o', color='blue', capsize=5)
    plt.axvline(0, linestyle='--', color='gray')
    plt.title('Confidence Interval for Difference in Means')
    plt.show()