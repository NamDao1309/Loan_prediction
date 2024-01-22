import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model, metrics

# Read data from csv file
csv_path = "Buoi25_DA.22.01.2024//nguoi.csv"
df = pd.read_csv(csv_path, index_col=0)
print(df)

# ve bieu do minh hoa dataset
# plt.plot(df['Cao'], df['Nang'], 'ro' )
# plt.xlabel('Chiều cao (cm)')
# plt.ylabel('Cân nặng (kg)')
# plt.show()

# sử dụng hồi quy tuyến tính
X = df.loc[:, ['Cao']].values # X là dữ liệu đầu vào
y = df['Nang'].values         # y là dữ liệu đầu ra

model = linear_model.LinearRegression() # loại model
model.fit(X, y)               # Huấn luyện/ tập huấn trên dữ liệu

# in một số thông tin về mô hình
mse = metrics.mean_absolute_error(model.predict(X), y)

print("Tổng bình phương sai trên tập mẫu :", mse)
print("Hệ số hồi quy:", model.coef_)
print("Sai số :", model.intercept_)
print(f"Công thức : [Nặng] ={model.coef_} x [Cao] + {model.intercept_}")

# vẽ lại sơ đồ
# plt.scatter(X, y, c='b')
# plt.plot(X, model.predict(X))
# plt.show()

# dự báo 1 số tình huống
while True:
    x = float(input("Nhập chiều cao ( nhập 0 để dừng)"))
    if x <= 0:
        break
    print("Người cao ", x, " cm, dự báo cân nặng là ", model.predict([[x]]))