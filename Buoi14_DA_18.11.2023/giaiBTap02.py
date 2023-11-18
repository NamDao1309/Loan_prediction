import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_path = "GITHUB//VIETECH_DA_28.09.2023//Buoi14_DA_18.11.2023//ketqua_soxo.csv"
new_csv_path = "GITHUB//VIETECH_DA_28.09.2023//Buoi14_DA_18.11.2023//new_ketqua_soxo.csv"

# 1. Đọc dữ liệu từ file csv, chuyển dữ liệu cột 1 sang date
df = pd.read_csv(csv_path, index_col=0, parse_dates=True)
print(df)

# 2. Xóa bỏ các dòng không có dữ liệu
df.dropna(inplace=True)

# 3. Thêm cột mới là 2 số cuối của giải độc đắc
df['SoDe'] = df.So % 100
# df.to_csv(new_csv_path)

# 4. Trích xuất cột mới thành dữ liệu series để dễ xử lý
s = pd.Series(df.SoDe, dtype='int64')
print(s)

# 5. Hiển thị phân bổ dữ liệu: biểu đồ histogram, 100 nhóm
s.plot(kind='hist', bins=100)
#plt.show()

# 6. Viết hàm tính số tiền thu về
def one_day(myNums, result, money):
    pay = len(myNums) * money
    get = money * 70 if result in myNums else 0
    return get - pay

def many_day(myNums, results, money):
    total = 0
    for x in results:
        total += one_day(myNums, x, money)
    return total

money = 1000
# thu chien luoc choi : nuoi 1 con
print("Chơi con 76 toàn bộ năm 2000 :", many_day([40], s[0:367], money))
print("Chơi con 76 toàn bộ các năm:", many_day([40], s, money))

print("Chơi nhiều số năm 2000 :", many_day([76, 92, 3, 10, 51, 45], s[0:367], money))
print("Chơi nhiều số toàn bộ các năm:", many_day([76, 92, 3, 10, 51, 45], s, money))

# Thống kê con ra nhiều nhất rồi chơi
x = s[0:367].value_counts().idxmax()
y = s.value_counts().idxmax()
print(" Chơi theo số ra nhiều nhất năm 2000 :", x, many_day([x], s, money))
print("Chơi theo số ra nhiều nhất các năm :", y, many_day([y], s, money))

# chơi ngẫu nhiên mỗi ngày 1 con
total =0
for day in s:
    total -= money
    m = np.random.randint(100)
    if( m == day): total += 70* money

print("Chơi ngẫu nhiên :", total)