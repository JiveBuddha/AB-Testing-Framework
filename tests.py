import pandas as pd
from ab_testing import ABTest
from visualization import plot_ab_histogram, plot_confidence_interval

# Sample data: Two groups with a metric (e.g., conversion rate)
data = {
    'group': ['control'] * 50 + ['treatment'] * 50,
    'conversion_rate': [0.12, 0.15, 0.10, 0.13, 0.14] * 10 + [0.18, 0.19, 0.17, 0.20, 0.22] * 10
}

df = pd.DataFrame(data)

# Initialize AB Test
ab_test = ABTest(df, group_col='group', metric_col='conversion_rate')

# Summarize data
summary = ab_test.summarize_data()
print("Summary statistics:")
print(summary)

# Perform t-test
ttest_result = ab_test.perform_ttest()
print("\nT-test result:")
print(ttest_result)

# Calculate confidence interval
ci_lower, ci_upper = ab_test.confidence_interval()
print(f"\nConfidence interval: ({ci_lower}, {ci_upper})")

# Visualize results
plot_ab_histogram(df, 'group', 'conversion_rate')
plot_confidence_interval(ci_lower, ci_upper)