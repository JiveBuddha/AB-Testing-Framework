import pandas as pd
import numpy as np
from scipy import stats

class ABTest:
    def __init__(self, data, group_col, metric_col):
        """
        Initialize the A/B Test framework.

        :param data: pd.DataFrame - The dataset for A/B testing
        :param group_col: str - Column name representing the A/B group (e.g., 'control', 'treatment')
        :param metric_col: str - Column name representing the metric (e.g., conversion rate)
        """
        self.data = data
        self.group_col = group_col
        self.metric_col = metric_col

    def summarize_data(self):
        """
        Summarizes data by group.

        :return: pd.DataFrame - Summary statistics for each group
        """
        summary = self.data.groupby(self.group_col)[self.metric_col].agg(['mean', 'std', 'count']).reset_index()
        return summary

    def perform_ttest(self, alpha=0.05):
        """
        Perform an independent t-test between the two groups.

        :param alpha: float - Significance level
        :return: dict - Test statistics and p-value
        """
        group_data = self.data.groupby(self.group_col)[self.metric_col].apply(list)
        t_stat, p_value = stats.ttest_ind(group_data[0], group_data[1])

        result = {
            't_statistic': t_stat,
            'p_value': p_value,
            'significant': p_value < alpha
        }
        return result

    def confidence_interval(self, confidence=0.95):
        """
        Calculate the confidence interval for the difference between the means of the two groups.

        :param confidence: float - Confidence level
        :return: tuple - Lower and upper bound of the confidence interval
        """
        group_stats = self.summarize_data()

        # Means and standard errors
        diff_mean = group_stats['mean'].iloc[1] - group_stats['mean'].iloc[0]
        se_diff = np.sqrt((group_stats['std'].iloc[0]**2 / group_stats['count'].iloc[0]) + 
                          (group_stats['std'].iloc[1]**2 / group_stats['count'].iloc[1]))

        # Critical value from normal distribution
        z_value = stats.norm.ppf(1 - (1 - confidence) / 2)
        margin_error = z_value * se_diff

        return (diff_mean - margin_error, diff_mean + margin_error)