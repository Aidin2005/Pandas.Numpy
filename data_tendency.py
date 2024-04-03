#Explain the major central and variance of data (like Percentiles, Standard Deviation, Variance, Correlation, Correlation Matrix, Correlation vs Causality) with python code

#Mean (Central Tendency):
    #The mean is the sum of all the values in a dataset divided by the number of values. It represents the average value of the dataset.
#Median (Central Tendency):
    #The median is the middle value of a dataset when it is ordered from least to greatest. If there is an even number of observations, the median is the average of the two middle values.
#Mode (Central Tendency):
    #The mode is the value that appears most frequently in a dataset.
#Percentiles:
    #Percentiles are used to divide a dataset into 100 equal parts. For example, the 25th percentile is the value below which 25% of the observations fall.
#Variance (Variability):
    #Variance measures how spread out the values in a dataset are from the mean. It is the average of the squared differences from the mean.
#Standard Deviation (Variability):
    #Standard deviation is the square root of the variance. It measures the average distance of each data point from the mean.
#Correlation:
    #Correlation measures the strength and direction of the linear relationship between two variables. It ranges from -1 to 1, where -1 indicates a perfect negative correlation, 0 indicates no correlation, and 1 indicates a perfect positive correlation.
#Correlation Matrix:
    #A correlation matrix is a table that shows the correlation coefficients between many variables in a dataset.
#Correlation vs. Causality:
   #Correlation does not imply causation. Just because two variables are correlated does not mean that changes in one variable cause changes in the other.

import numpy as np
import scipy.stats

# Sample dataset
data = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

# Mean
mean = np.mean(data)
print("Mean:", mean)

# Median
median = np.median(data)
print("Median:", median)

# Mode
mode, mode_count = scipy.stats.mode(data)
if isinstance(mode, np.ndarray):
    print("Modes (with frequencies):")
    for value, count in zip(mode, mode_count):
        print("Value:", value, "Frequency:", count)
else:
    print("Mode:", mode)

# Percentiles
percentiles = np.percentile(data, [25, 50, 75])
print("25th Percentile:", percentiles[0])
print("50th Percentile (Median):", percentiles[1])
print("75th Percentile:", percentiles[2])

# Variance
variance = np.var(data)
print("Variance:", variance)

# Standard Deviation
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

# Correlation
data2 = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
correlation = np.corrcoef(data, data2)[0, 1]
print("Correlation coefficient:", correlation)

# Correlation Matrix
import pandas as pd


data = {
    'Age': [30, 35, 40, 45, 50],
    'Salary': [50000, 60000, 70000, 80000, 90000],
    'Experience': [5, 7, 10, 12, 15]
}

df = pd.DataFrame(data)

correlation_matrix = df.corr()

print("correlation matrix:")
print(correlation_matrix)
