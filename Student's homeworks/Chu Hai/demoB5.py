# dict = {
#     'brand' : 'toyota',
#     'year': '2018',
#     'mau' : 'do',
#     'gia' : '50000',

# }
# print(dict['brand'])
# dict['brand'] = 'ford'
# print(dict)
# print(len(dict)) #đến số phần tử dict
# print(type(dict))


# #truy cập phần từ dict
# print(dict['mau'])

# #phan tử keys
# print(dict.keys())
# #list phan tử kết quả
# print(dict.values())

# #update keys
# dict.update({'mau':'xanh'})

# print(dict) #check

# #thêm phần tử vào dict
# dict['power'] = 500
# dict['country'] = ['Vietnam','Nhat','TQ']
# print(dict)

# #xóa phần tử khỏi dict

# dict.pop('country')
# print(dict)
# #hoặc có thể dùng del dict
# del dict['power']
# print(dict)
# # #xóa hẳn dict
# # dict.clear()

# #duyệt các phần tử dict

# for x in dict:
#    # print(x) #in ra key
#      print(dict[x]) #hiển thị kết quả value

# for y in dict.keys(): #cách khác để in key thay dict.values()
#      print(y)
# for x,y in dict.items(): #in ra theo thứ tự tương ứng
#      print(x,y)

#  # copy 1 tệp giá trị khác    
# dict2={}# copy 1 tệp giá trị khác
# dict2= dict.copy() # copy 1 tệp giá trị khác

#####################################################
# bài tập text= 'một năm có mười hai tháng,
# tháng hai có hai mươi tám ngày, các tháng còn lại có ba mươi hoặc ba mươi mốt ngày'
# Đếm số tần suất hiện của các từ trong câu.

# Câu cần đếm từ
text = "Một năm có mười hai tháng, tháng hai có hai mươi tám ngày, các tháng còn lại có ba mươi hoặc ba mươi một ngày"

# Chia câu thành các từ
text= text.lower()

words = text.split()

# Sử dụng một từ điển để đếm số lần xuất hiện của mỗi từ
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# In số lần xuất hiện của từng từ
for word, count in word_count.items():
    print(f"'{word}': {count} lần")
#######################################################
# tính giá nước sinh hoạt với mức giá : 0-10 m3 giá 5000 đ/m3
# 10-20 m3 giá 7000 đ/m3
# 20-30 m3 giá 9000 đ/m3
# trên 30m3 giá 16000 đ/m3
# viết trương trình đầu vào nhập khối lượng nước đầu ra tính chi phí tương ứng với mức giá và tính tổng số tiền
# Đầu vào: Nhập khối lượng nước
m3 = float(input("Nhập khối lượng nước (m3): "))

# Khai báo biến để lưu tổng chi phí
total_cost = 0

# Mức giá nước
price_tien = [(0, 10, 5000), (10, 20, 7000), (20, 30, 9000), (30, None, 16000)]

# Tính chi phí dựa trên mức giá
# for tien in price_tien:
#     start, end, price = tien
#     if end is None:
#         # Mức giá cuối cùng (trên 30m3)
#         if water_use > start:
#             total_cost += (water_use - start) * price
#     else:
#         # Các mức giá khác
#         if start <= water_use <= end:
#             total_cost += water_use * price
#         elif water_use > end:
#             total_cost += (end - start) * price
if(0<= m3 <=10)

# In tổng chi phí
print(f"Chi phí nước là: {total_cost:.2f} đồng")
# dang sai công thức tính tiền

