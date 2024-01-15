import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

csv_path = "Buoi22_DA.08.01.2024\Data.csv"
df = pd.read_csv(csv_path, usecols=['Age', 'Salary'])

df['Age'].fillna((df['Age'].mean()), inplace=True)
df['Salary'].fillna((df['Salary'].mean()), inplace=True)

# SU DUNG MINMAXSCALER
# print(df)

# scaler = MinMaxScaler()
# scaled = scaler.fit_transform(df)

# print(scaled)
# plt.figure(figsize=(12,8))
# sns.distplot(df['Salary'])
# print("Do lech chuan Salary : % s" % (statistics.stdev(df['Salary'])))
# plt.show()


# SU DUNG STANDARDLIZATION
sc_data = StandardScaler()
std_sc_data = sc_data.fit_transform(df)
print(std_sc_data)

plt.figure(figsize=(12,8))
sns.distplot(df['Salary'])
print("Do lech chuan Salary : % s" % (statistics.stdev(df['Salary'])))
plt.show()