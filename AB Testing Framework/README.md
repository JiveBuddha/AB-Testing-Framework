# A/B Testing Framework

## Overview
This A/B Testing Framework allows you to perform statistical analysis on A/B test data. It helps in summarizing the test results, performing a t-test to check for statistical significance, and calculating confidence intervals. Additionally, it includes visualization tools to present your A/B test results effectively.

The framework is designed to be flexible, allowing users to define their own A/B groups and metrics for analysis. It is built using Python and leverages libraries such as Pandas, NumPy, SciPy, and Matplotlib for data manipulation and visualization.

## Features
- **Data Summarization**: Provides summary statistics (mean, standard deviation, count) for each group.
- **T-Test**: Performs an independent t-test to determine if there is a statistically significant difference between groups.
- **Confidence Interval**: Calculates a confidence interval for the difference in means between the two groups.
- **Visualization**: Plots histograms of the metric distributions and visualizes confidence intervals for the difference in means.

## Installation
To get started, clone the repository and install the required dependencies using the `requirements.txt` file:

```bash
git clone https://github.com/yourusername/ab_testing_framework.git
cd ab_testing_framework
pip install -r requirements.txt