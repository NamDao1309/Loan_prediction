import pandas as pd 
import numpy as np

csv_path = "Buoi19_DA.25.12.2023\horse-colic.csv"
new_csv_path = "Buoi19_DA.25.12.2023\processing_horse-colic.csv"
csv_iris_path = "Buoi19_DA.25.12.2023\iris.csv"

# df_iris = pd.read_csv(csv_iris_path, header=None)
# print(df_iris.head())

# # CHECK NULL
# # Cach 1: isnull()
# print(df_iris.isnull())

# # Cach 2 : isna()
# print(df_iris.isna())

# # Cach 3 : isna().any()
# print(df_iris.isna().any())

# # cach 4: isna().sum()
# print(df_iris.isna().sum())

# # HANDLE MISSING DATA

# #Cach 1 : delete rows/ columns containing missing data
# # Hien thi kich thuoc truoc khi drop
# print(df_iris.shape)

# # drop data
# df_iris.dropna(inplace=True)

# # Hien thi kich thuoc sau khi drop
# print(df_iris.shape)

df_horse_colic = pd.read_csv(csv_path, header=None, na_values = '?')
for i in range(df_horse_colic.shape[1]):
    # count number of rows with missing values
    n_miss = df_horse_colic[i].isnull().sum()
    percent = (n_miss/ df_horse_colic.shape[0]) * 100
    print('Row :%d, Missing %d (%.1f%%)' % (i, n_miss, percent))

# processing missing data
for j in range(df_horse_colic.shape[1]):
    n_missing_rows = df_horse_colic[j].isnull().sum()
    percent_missing_rows = (n_missing_rows/ df_horse_colic.shape[0])* 100

    if(percent_missing_rows < 5):
        df_horse_colic.drop(j, inplace=True)

    print(' Rows : %d, Missing vaule : %d, rate : (%.1f%%)' % (j, n_missing_rows, percent_missing_rows))
df_horse_colic.to_csv(new_csv_path)