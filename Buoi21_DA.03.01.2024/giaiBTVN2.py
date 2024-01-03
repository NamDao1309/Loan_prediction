import pandas as pd
import numpy as np

csv_path ="Buoi21_DA.03.01.2024\data_obsity.csv"

df = pd.read_csv(csv_path)

print(df.head(5))
print(df.columns)
print(df.shape)

# print(df.index.to_list())
df.drop([0, 1, 2], inplace=True)

columns_to_drop = df.filter(regex='[0-9]+\.[1-2]')
df.drop(columns= columns_to_drop, inplace=True)
print(df)