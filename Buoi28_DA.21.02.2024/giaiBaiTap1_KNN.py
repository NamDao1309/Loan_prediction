from sklearn import neighbors
import pandas as pd
import numpy as np

# doc du lieu tu file csv
csv_path = "Buoi28_DA.21.02.2024//population.csv"
df = pd.read_csv(csv_path)
print(df)

# su dung support vector machine
X = df.loc[:, ['Year']].values  # X là năm, dữ liệu đầu vào
y = df['Population'].values       # y là dân số,  dữ liệu đầu ra

# tạo model 
knn = neighbors.KNeighborsRegressor(n_neighbors=5)

# Model Fitting
knn.fit(X, y)

# dự báo dân số
while True:
    x = int(input("Nhập năm :"))
    if x <=0:
        break
    print("Dân số năm ", x, " được dự báo là :", knn.predict([[x]]))
