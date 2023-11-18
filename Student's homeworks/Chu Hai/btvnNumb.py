import csv
import numpy as np

file_path_winequalityred = "D:\DA\VIETECH_DA_28.09.2023\Student's homeworks\Chu Hai\winequality-red.csv"
file_path_winequalitywhite = "D:\DA\VIETECH_DA_28.09.2023\Student's homeworks\Chu Hai\winequality-white.csv"

with open(file_path_winequalityred, 'r') as f:
    #red_wines = list(csv.reader(f, delimiter=';'))
    red_wines = np.asarray(list(csv.reader(f, delimiter=';')))

with open(file_path_winequalitywhite, 'r') as f:
    white_wines = np.asarray(list(csv.reader(f, delimiter=';')))
    #white_wines = np.asarray(white_wines)

print(red_wines)


#hiển thị 5 hàng đầu, 5 hàng cuối

print(red_wines[:6])
print(white_wines[:6])

#tính trung bình chất lượng cảu rượu

quantiti_ruoudo =[float(item[-1]) for item in red_wines[1:]]
quantiti_ruoudo_medium =sum(quantiti_ruoudo)/len(quantiti_ruoudo)

print ("chat luong rượu đỏ",quantiti_ruoudo_medium)

quantiti_ruoutrang =[float(item[-1]) for item in white_wines[1:]]
quantiti_ruoutrang_medium =sum(quantiti_ruoutrang)/len(quantiti_ruoutrang)

print ("chat luong rượu trắng",quantiti_ruoutrang_medium)

4# xác định kích thước của mảng

print("kích thước bảng rươu đỏ",red_wines.shape)
print("kích thước bảng rươu trắng",white_wines.shape)

#5 tính trung bình chất lượng của rượu
print(red_wines[1:,-1].astype(float))
print(" trung bình của rượu đỏ", np.mean(red_wines[1:,-1].astype(float)))

print(white_wines[1:,-1].astype(float))
print(" trung bình của rượu trắng", np.mean(white_wines[1:,-1].astype(float)))

#6 chất lượng của rượu
print("lệch chuẩn std rượu đỏ", np.std(red_wines[1:,-1].astype(float)))
print(" lệch chuẩn std rượu trắng", np.std(white_wines[1:,-1].astype(float)))

#7 tính chất lượng min,max của rượu
print("min rượu đỏ", np.min(red_wines[1:,-1].astype(float)))
print("max rượu đỏ", np.max(red_wines[1:,-1].astype(float)))
#