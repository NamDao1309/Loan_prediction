import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# cau 1
csv_path ="GITHUB//VIETECH_DA_28.09.2023//Buoi14_DA_18.11.2023//hocsinh.csv"
df = pd.read_csv(csv_path, index_col=0)
print(df)

# Cau 2: In du lieu ra man hinh
print(df.head(5))
print(df.tail(5))

# Cau 3: Thong ke loai gioi
print(len(df[df.Diem >= 8]))

# Cau 4. Thông kê xem lớp có bao nhiêu bạn trượt môn
#  (điểm dưới 4 hoặc không có điểm)
print(len(df[(df.Diem < 4) | (df.Diem.isnull())]))

# Cau 5. Vẽ đồ thị histogram minh họa phân bổ 
# điểm số của lớp (trục giá trị từ 0 đến 10, không
# có điểm tính là 0)

df.Diem.plot(kind='hist', bins = 10)
# plt.show()

# Cau 6. Xử lý những ô điểm trống bằng cách fill giá trị 0 vào ô
df.Diem.fillna(0, inplace=True)

# Cau 7: 7. Thống kê theo loại điểm, 
# so sánh xem khác với biểu đồ histogram ở điểm nào
df.Diem.value_counts().sort_index().plot(kind='bar')
plt.show()


