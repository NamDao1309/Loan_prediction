import math
#bai 2_1
# bài toán tam giác
# a = int(input("Nhập a = "))
# b = int(input("Nhập b = "))
# c = int(input("Nhập c = "))
# p = (a+b+c)/2
# S = math.sqrt(p*(p-a)*(p-b)*(p-c)) 
# s = (a*b)/2
# if (a + b) > c and (b + c) > a and (a + c) > b:
#     if a == b == c:
#         print("Đây là tam giác đều")
#         print("Diện tích tam giác là" ,S)

#     elif a == b or a == c or b == c:
#         print("Đây là tam giác cân")
#         print("Diện tích tam giác là" ,S)

#     elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         print("Đây là tam giác vuông")
#         print("Diện tích tam giác là" ,s)
    
#     else:
#         print("Đây là tam giác thường")
#         print("Diện tích tam giác là" ,S)

# else:
#     print("Đây không phải là 3 cạnh của tam giác")


#bai 2_2
# x = int(input("Nhap vao so tu 1 den 10: "))
# if(x == 8):
#     print("Chủ nhật")
# elif(x == 2):
#     print("Thứ hai")
# elif(x == 3):
#     print("Thứ ba")
# elif(x == 4):
#     print("Thứ tư")
# elif(x == 5):
#     print("Thứ năm")
# elif(x == 6):
#     print("Thứ sáu")
# elif(x == 7):
#     print("Thứ bảy")
# else:
#     print("Đây không phải là ngày trong tuần")

#bai 2_3
# x = int(input("Nhập số bất kì từ 1 đến 12: "))
# if(x == 1):
#     print("Đây là tháng 1 có 31 ngày")
# elif(x == 2):
#     print("Đây là tháng 2 có 28 hoặc 29 ngày")
# elif(x == 3):
#     print("Đây là tháng 3 có 31 ngày")
# elif(x == 4):
#     print("Đây là tháng 4 có 30 ngày")
# elif(x == 5):
#     print("Đây là tháng 3 có 31 ngày")
# elif(x == 6):
#     print("Đây là tháng 3 có 30 ngày")
# elif(x == 7):
#     print("Đây là tháng 3 có 31 ngày")
# elif(x == 8):
#     print("Đây là tháng 3 có 31 ngày")
# elif(x == 9):
#     print("Đây là tháng 3 có 30 ngày")
# elif(x == 10):
#     print("Đây là tháng 3 có 31 ngày")
# elif(x == 11):
#     print("Đây là tháng 3 có 30 ngày")
# elif(x == 12):
#     print("Đây là tháng 3 có 31 ngày")
# else:
#     print("Đây không phải là tháng trong năm")

#bai2_4
# a = int(input("Nhap số thứ nhất: "))
# b = int(input("Nhập số thứ hai: "))
# c = int(input("Nhập số thứ ba: "))
# d = int(input("Nhập số thứ tư: "))

# if (a > b and a > c and a > d):
#     print("Số lớn nhất là " , a)
# elif (b > a and b > c and b > d):
#     print("Số lớn nhất là " ,b)
# elif (c > a and c > b and c > d):
#     print("Số lớn nhất là " ,c)
# else:
#     print("Số lớn nhất là: ",d)

#bai2_5
# a = int(input("Nhập thang bat ki = "))
# if (a >= 1 and a <= 3):
#     print("Mua xuan")
# elif (a >= 4 and a <= 6):
#     print("Mua he")
# elif (a >= 7 and a <= 9):
#     print("Mua thu")
# elif (a >= 10 and a <= 12):
#     print("Mua dong")
# else: 
#     print("Day khong phai la thang. Moi ban nhap lai")

#bai2_6
# km = int(input("Nhap so km: "))
# if (km == 1):
#     soTien = 5000
#     print("So tien phai tra la: " ,soTien)
# elif (km >1 and km <= 5):
#     soTien = (km - 1) * 4500 + 5000
#     print("So tien phai tra la: " ,soTien)
# elif (km > 5 and km <= 120):
#     soTien = (km - 5)*3500 + 4500*4 + 5000
#     print("So tien phai tra la: " ,soTien)
# else:
#     soTien = (((km - 5)*3500 + 4500 * 4 + 5000))
#     print("So tien phai tra la: " ,soTien)

#bai 2_7
# h = int(input("Nhập số giờ dùng máy: "))
# tg = int(input("Nhập khung giờ dùng: "))
# if(tg >= 0 and tg <= 7):
#     if (h == 7):
#         tien = h * 5000 * 300 * 60
#         print("Tiền giờ sử dụng là ",tien)
#     else:
#         tien = h * 5000 * 300
#         print("Tiền giờ sử dụng là ",tien)
# elif(tg > 7 and tg <= 17):
#     if (h >= 6):
#         tien = (h * 5000 * 400 * 60)/ 0.1
#         print("Tiền giờ sử dụng là ",tien) 
#     else:
#         tien =  h * 5000 * 400
#         print("Tiền giờ sử dụng là ",tien)
# else:
#     if (h >= 4):
#         tien = (h * 5000 * 350 * 60)/0.12
#         print("Tiền giờ sử dụng là ",tien)
#     else:
#         tien = h * 5000 * 350
#         print("Tiền giờ sử dụng là ",tien)

#bai 2_8
# tienVay = 400000000
# laiSuatHN = 0.1
# tienTraMT = 10000000

# thang = 0
# while(tienVay > 0):
#     if (thang == 0):
#         laiSuat  = 0
#     else:
#         laiSuat = tienVay * (laiSuatHN / 12)
#     tienVay += laiSuat
#     tienVay -= tienTraMT
#     thang += 1
# print("Người mua căn hộ sẽ thanh toán hết nợ sau" ,thang , "tháng")

#bai 2_9
# a = int(input("Nhập số cần tính tổng: "))
# tong = 0
# while(a > 0):
#     chuSo = a % 10
#     tong += chuSo
#     a //= 10

# print("Tổng các chữ số là:",tong)

#bai 2_10
# a = int(input("Nhập số cần đảo: "))
# soDao = 0
# while(a > 0):
#     chuSo = a % 10
#     soDao = soDao * 10 + chuSo
#     a //= 10
# print("Số sau khi đảo là",soDao)

#bai 2_11
# n = 3
# i = 1
# while (i <= n):
#     j = 1
#     while j <= i:
#         print("*", end=' ')
#         j += 1
#     print()
#     i += 1

#bai 2_12
# n = 5
# i = 1
# while (i <= n):
#     j = 1
#     while j <= i:
#         print(j, end=' ')
#         j += 1
#     print()
#     i += 1

#bai 2_13
# a = int(input("Nhập số cần tính tổng: "))
# tong = 0
# i = 1
# while(i <= a):
#     tong += i
#     i = i + 1
# print("Tong la",tong)

#bai 2_14
# n = 5
# i = n
# while i >= 1:
#     j = i
#     while j >= 1:
#         print(j, end=' ')
#         j -= 1
#     print()
#     i -= 1

#bai 2_15
# a, b = 0, 1
# count = 20
# print(a, b, end=' ')

# while count > 2:
#     c = a + b
#     print(c, end=' ')
#     a, b = b, c
#     count -= 1

#bai 2_16
n = 5
i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=' ')
        j += 1
    print()
    i += 1
n = 4
i = n
while i >= 1:
    j = i
    while j >= 1:
        print("*", end=' ')
        j -= 1
    print()
    i -= 1
