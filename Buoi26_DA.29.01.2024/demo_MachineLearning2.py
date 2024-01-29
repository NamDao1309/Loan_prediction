import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model, metrics

# doc du lieu tu file csv
csv_path = "Buoi26_DA.29.01.2024//nguoi2.csv"
df = pd.read_csv(csv_path, index_col=0)
print(df)

# them cot gioi tinh Nam = 1, goi tinh Nu = 0
df['GT'] = df['GioiTinh'].apply(lambda x: 1 if x =='Nam' else 0)

# su dung hoi quy tuyen tinh
X = df.loc[:, ['Cao', 'GT']].values # X la du lieu dau vao
y = df['Nang'].values  # y la du lieu dau ra
model = linear_model.LinearRegression()  # loai model
model.fit(X, y)     # huan luyen tren du lieu

# hien thi mot so thong tin ve model
mse = metrics.mean_absolute_error(model.predict(X), y)

print("Tổng bình phương sai số trên tập mẫu :", mse)
print("Hệ số hồi quy :", model.coef_)
print("Sai số :", model.intercept_)
print(f"Công thức : [Nặng] = {model.coef_} x [Cao, Giới tính] + {model.intercept_}")

# dự báo 1 số tình huống
while True:
    x = float(input("Nhập chiều cao :"))
    if x <= 0: break
    print("Nam giới cao :", x , " và cân nặng dự báo là :", model.predict([[x, 1]]))
    print("Nữ giới cao :", x , " và cân nặng dự báo là :", model.predict([[x, 0]]))