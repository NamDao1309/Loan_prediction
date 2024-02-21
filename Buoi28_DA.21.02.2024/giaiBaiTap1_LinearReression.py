from sklearn import linear_model
import pandas as pd
import numpy as np

# doc du lieu tu file csv
csv_path = "Buoi27_DA.19.02.2024//population.csv"
df = pd.read_csv(csv_path)
print(df)

# su dung hoi quy tuyen tinh
X = df.loc[:, ['Year']].values   # X là năm, dữ liệu đầu vào
y =df['Population'].values       # y là dân số,  dữ liệu đầu ra

model = linear_model.LinearRegression() # loại model
model.fit(X, y)                         # Huấn luyện/ training trên dữ liệu

# dự báo dân số
while True:
    x = int(input("Nhập năm :"))
    if x <=0:
        break
    print("Dân số năm ", x, " được dự báo là :", model.predict([[x]]))