import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Đọc dữ liệu từ file csv và chuyển cột 1 sang dạng ngày tháng
csv_path = "buổi 14\ketqua_soxo.csv"
csv_path2="buổi 14\ketquanew.csv"
df = pd.read_csv(csv_path, index_col=0,parse_dates=[1])
print(df)

#2 Xóa bỏ các dòng không có dữ liệu
df.dropna(inplace=True)

# 3Thêm cột mới là 2 số cuối của giải độc đắc
df['SoDe'] = df['So'].astype(str).str[-2:]
# df.to_csv(ketquanew.csv)
# print(df)
# 4 Trích xuất cột mới thành dữ liệu series
s= pd.Series(df.SoDe, dtype='int64')
print(s)

#5Hiển thị phân bổ dữ liệu: biểu đồ histogram, 100 nhóm
s.plot(kind='hist',bins=100)
plt.show()

#6 Viết hàm tính số tiền thu về
def one_day(myNums,result,money):
    pay = len(myNums)*money
    get= money*70 if result in myNums else 0
    return get-pay
def many_day(myNums, result,money):
    total = 0
    for x in result:
        total+= one_day(myNums,x,money)
    return total

