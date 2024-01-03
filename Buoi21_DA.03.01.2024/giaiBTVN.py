import pandas as pd
import numpy as np

csv_path ="Buoi21_DA.03.01.2024\data.csv"
new_csv_path ="Buoi21_DA.03.01.2024\data_new.csv"
df =pd.read_csv(csv_path)
# print(df)

# xu ly gia tri bat thuong
for index in df.index:
    if df.loc[index, "Duration"] > 120:
        df.loc[index, "Duration"] = 120

# xu ly duplicate
df.drop_duplicates(inplace=True)

# xu ly gia tri null
df.dropna(inplace=True)

# export csv file
df.to_csv(new_csv_path)

df1 = pd.read_csv(new_csv_path)

# xu ly du lieu dat khong dung dinh dang
print(df1)

