import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cau 1
csv_path = r"D:\DA\VIETECH_DA_28.09.2023\Student's homeworks\Chu Hai\buổi 14\hocsinh.csv"
df = pd.read_csv(csv_path)
print(df)

#cau 2
print(df.head(5))
print(df.tail(5))

#câu 3

# Đếm số lượng học sinh có điểm từ 8 trở lên
so_luong_diem_gioi = df[df['Diem'] >= 8].shape[0]

# In số lượng học sinh có điểm từ 8 trở lên ra màn hình
print("Số lượng học sinh có điểm loại giỏi (điểm từ 8 trở lên) trong lớp là:", so_luong_diem_gioi)

#câu 4
# Đếm số lượng học sinh có điểm dưới 4 hoặc không có điểm
so_luong_hoc_sinh_truot = df[(df['Diem'] < 4) | (df['Diem'].isnull())].shape[0]

# In số lượng học sinh có điểm dưới 4 hoặc không có điểm ra màn hình
print("Số lượng học sinh trượt môn (điểm dưới 4 hoặc không có điểm) trong lớp là:", so_luong_hoc_sinh_truot)

#câu 5
#Câu 6 Xóa các dòng có giá trị NaN và thay thế bằng 0
df['Diem'].fillna(0, inplace=True)

#Vẽ đồ thị histogram
plt.hist(df['Diem'], bins=11, range=(0, 11), edgecolor='red')
plt.xlabel('Điểm')
plt.ylabel('Số lượng học sinh')
plt.title('Phân bổ điểm số của lớp')
#plt.show()
#cách 2
df.Diem.plot(kind='hist', bins=10)
#plt.show()

#câu 7  Thống kê theo loại điểm, so sánh xem khác 
# với biểu đồ histogram ở điểm nào
df.Diem.value_counts().sort_index().plot(kind='bar')
plt.show()