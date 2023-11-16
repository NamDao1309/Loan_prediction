#BÀI 2.7: Thực hành numpy với file dữ liệu về rượu vang đỏ và trắng được cho đính kèm
#sau : winequality-red.csv và winequality-white.csv
#1. Đọc dữ liệu thông tin từ file winequality-red.csv, lưu thông tin vào 1 mảng
#2. Hiển thị 5 hàng đầu và 5 hàng cuối của dữ liệu
#3. Tính trung bình chất lượng (quality) của rượu
#4. Xác định kích thước của mảng
#5. Tính trung bình chất lượng (quality ) của rượu
#6. Tính độ lệch chuẩn chất lượng (quality ) của rượu
#7. Tìm chất lượng nhỏ nhất (quality ) của rượu
#8. Tìm chất lượng lớn nhất (quality ) của rượu
#9. Tìm các hàng có chất lượng rượu > 7
#10. Hiển thị rượu với độ cồn alcohol > 10 và quality > 7
#11. Kết hợp rượu đỏ và rượu trắng vào mảng all_wines, hiển thị kích thước của mảng

import csv
import numpy as np

file_path_winequality_red = "GITHUB\VIETECH_DA_28.09.2023\Buoi11_DA_08.11.2023\winequality-red.csv"
file_path_winequality_white = "GITHUB\VIETECH_DA_28.09.2023\Buoi11_DA_08.11.2023\winequality-white.csv"

#1. Đọc dữ liệu thông tin từ file winequality-red.csv, lưu thông tin vào 1 mảng
with open(file_path_winequality_red, 'r') as f:
    red_wines = np.asarray(list(csv.reader(f, delimiter=';')))
    #red_wines = list(csv.reader(f, delimiter=';'))

with open(file_path_winequality_white, 'r') as f:
    white_wines = np.asarray(list(csv.reader(f, delimiter=';')))
    #white_wines = list(csv.reader(f, delimiter=';'))

# print(red_wines)
# print(white_wines)

#2. Hiển thị 5 hàng đầu và 5 hàng cuối của dữ liệu
print(red_wines[:6])
print(white_wines[:6])

#3. Tính trung bình chất lượng (quality) của rượu
quantities_red_wines = [float(item[-1]) for item in red_wines[1:]]
quantities_red_wines_medium = sum(quantities_red_wines)/len(quantities_red_wines)

print("Trung bình quality rượu đỏ:", quantities_red_wines_medium)

quantities_white_wines = [float(item[-1]) for item in white_wines[1:]]
quantities_white_wines_medium = sum(quantities_white_wines)/len(quantities_white_wines)

print("Trung bình quality rượu trắng:", quantities_white_wines_medium)

#4. Xác định kích thước của mảng

print("Kích thước mảng rượu đỏ :", red_wines.shape)
print("Kích thước mảng rượu trắng :", white_wines.shape)

#5. Tính trung bình chất lượng (quality ) của rượu
print(red_wines[1:, -1])
print("Trung bình quality rượu đỏ:", np.mean((red_wines[1:, -1]).astype(float)))
print("Trung bình quality rượu trắng:", np.mean((white_wines[1:, -1]).astype(float)))

#6. Tính độ lệch chuẩn chất lượng (quality ) của rượu
print("Độ lệch chuẩn std rượu đỏ:", np.std((red_wines[1:, -1]).astype(float)))
print("Độ lệch chuẩn std rượu trắng:", np.std((white_wines[1:, -1]).astype(float)))

#7. Tìm chất lượng nhỏ nhất (quality ) của rượu
print("chất lượng nhỏ nhất rượu đỏ:", np.min((red_wines[1:, -1]).astype(float)))
print("chất lượng nhỏ nhất rượu trắng:", np.min((white_wines[1:, -1]).astype(float)))


#8. Tìm chất lượng lớn nhất (quality ) của rượu
print("chất lượng lớn nhất rượu đỏ:", np.max((red_wines[1:, -1]).astype(float)))
print("chất lượng lớn nhất rượu trắng:", np.max((white_wines[1:, -1]).astype(float)))

#9. Tìm các hàng có chất lượng rượu > 7

high_quality_red = red_wines[1:, 11].astype(float)
print(high_quality_red[high_quality_red> 7])

high_quality_white = white_wines[1:, 11].astype(float)
print(high_quality_white[high_quality_white> 7])

#10. Hiển thị rượu với độ cồn alcohol > 10 và quality > 7
high_quality_and_alcohol = red_wines[1:, 10:].astype(float)
print(high_quality_and_alcohol[high_quality_and_alcohol[:,0]>10] and high_quality_and_alcohol[high_quality_and_alcohol[:,1]>7])

