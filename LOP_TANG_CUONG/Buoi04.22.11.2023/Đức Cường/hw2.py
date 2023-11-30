# Bài 2.1
# import math
# a = float(input("Nhập a = "))
# b = float(input("Nhập b = "))
# c = float(input("Nhập c = "))
# p = (a + b + c)/2
# s = math.sqrt(p*(p - a)*(p - b)*(p - c))
# if a + b > c and b + c > a and a + c > b:
#     if a == b == c:
#         print("Đây là tam giác đều", "s = ", s)
#     elif a == b or a == c or b == c:
#         print("Đây là tam giác cân", "s = ", s)
#     elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         print("Đây là tam giác vuông", "s = ", s)
#     else:            
#         print("Đây là tam giác thường", "s = ", s)
# else: 
#     print("Không phải là tam giác")        

# Bài 2.2
# n = int(input("Nhập n = "))
# if n == 2:
#     print("Thứ hai")
# elif n == 3:
#     print("Thứ ba")
# elif n == 4:
#     print("Thứ tư")
# elif n == 5:
#     print("Thứ năm")
# elif n == 6:
#     print("Thứ sáu")
# elif n == 7:
#     print("Thứ bảy")
# elif n == 8:
#     print("Chủ nhật")
# else:
#     print("Không phải ngày trong tuần")    

# Bài 2.3
# x = int(input("Nhập x = "))
# if x == 1:
#     print("Đây là tháng 1 có 31 ngày")
# elif x == 2:
#     print("Đây là tháng 2 có 28 hoặc 29 ngày")
# elif x == 3:
#     print("Đây là tháng 3 có 31 ngày")
# elif x == 4:
#     print("Đây là tháng 4 có 30 ngày")
# elif x == 5:
#     print("Đây là tháng 5 có 31 ngày")
# elif x == 6:
#     print("Đây là tháng 6 có 30 ngày")
# elif x == 7:
#     print("Đây là tháng 7 có 31 ngày")
# elif x == 8:
#     print("Đây là tháng 8 có 31 ngày")
# elif x == 9:
#     print("Đây là tháng 9 có 30 ngày")
# elif x == 10:
#     print("Đây là tháng 10 có 31 ngày")
# elif x == 11:
#     print("Đây là tháng 11 có 30 ngày")
# elif x == 12:
#     print("Đây là tháng 12 có 31 ngày")
# else:
#     print("Đây không phải tháng trong năm")

# Bài 2.4
# a = float(input("Nhập a = "))
# b = float(input("Nhập b = "))
# c = float(input("Nhập c = "))
# d = float(input("Nhập d = "))
# if a > b and a > c and a > d:
#     print(a, "là max")
# elif b > a and b > c and b > d:
#     print(b, "là max")
# elif c > b and c > d and c > a:
#     print(c, "là max")
# else:
#     print(d, "là max") 

# Bài 2.5  
# x = int(input("Nhập x = "))
# if x >= 1 and x <= 3:
#     print("Đây là mùa xuân")
# elif x >= 4 and x <= 6:
#     print("Đây là mùa hè")
# elif x >= 7 and x <= 9:
#     print("Đây là mùa thu")
# elif x >= 10 and x <= 12:
#     print("Đây là mùa đông")
# else:
#     print("Đây không phải tháng")

# Bài 2.6
# x = float(input("Nhập x = "))
# if x <= 1:
#     s = 5000
#     print("Số tiền là:",s,"đ")
# elif x > 1 and x <= 5:
#     s = (x - 1)*4500 + 5000
#     print("Số tiền là:",s,"đ")
# elif x > 5 and x <= 120:
#     s = (x - 5)*3500 + 4500*4 + 5000
#     print("Số tiền là:",s,"đ")
# else:
#     s = ((x - 5)*3500 + 4500*4 + 5000)*1/10
#     print("Số tiền là:",s,"đ")

# Bài 2.7
# x = float(input("Mốc thời gian sử dụng máy tính: "))
# if x >= 0 and x <= 7:
#     a = float(input("Số giờ sử dụng máy tính: "))    
#     if a >= 7 and a <= 8:
#         s = a*5000*300*60/0.15
#         print("Số tiền giờ dùng máy tính: ",s,"đ")
#     elif a < 7 and a >= 0:
#         s = a*5000*300
#         print("Số tiền giờ dùng máy tính: ",s,"đ")
#     else:
#         print("Lỗi")
# elif x > 7 and x <= 17:
#     b = float(input("Số giờ sử dụng máy tính: "))
#     if b >= 6 and b <= 10:
#         s = b*5000*400*60/0.1
#         print("Số tiền giờ dùng máy tính: ",s,"đ")
#     elif b < 6 and b >= 0:
#         s = b*5000*400
#         print("Số tiền giờ dùng máy tính: ",s,"đ")
#     else:
#         print("Lỗi")
# elif x > 17 and x <= 24:
#     c = float(input("Số giờ sử dụng máy tính: "))
#     if c >= 4 and c <= 7:
#         s = c*5000*350*60/0.12
#         print("Số tiền giờ dùng máy tính: ",s,"đ")
#     elif c < 4 and c >= 0:
#         s = c*5000*350
#         print("Số tiền giờ dùng máy tính: ",s,"đ")
#     else:
#         print("Lỗi")
# else:
#     print("Lỗi")

# Bài 2.9
# a = int(input("Nhập số cần tính tổng: "))
# sum = 0
# while a > 0:
#     chuSo = a % 10
#     sum = sum + chuSo
#     a //= 10
# print("Tổng các chữ số là: ",sum)

# Bài 2.10
# a = int(input("Nhập số cần đảo ngược: "))
# b = 0
# while a > 0:
#     chuSo = a % 10
#     b = b*10 + chuSo
#     a //= 10
# print("Số đảo ngược là: ",b)

# Bài 2.11
# n = 3
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print("*", end = ' ')
#         j += 1
#     print()
#     i += 1

# Bài 2.12
# n = 5
# i = 1
# while i <= n:
#     j = 1 
#     while j <= i:
#         print(j, end = ' ')
#         j += 1
#     print()
#     i += 1

# Bài 2.13
# n = int(input("Nhập số cần tính tổng: "))
# i = 0
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print("Tổng: ", sum)

# Bài 2.14
# n = 5
# i = n
# while i >= 1:
#     j = i
#     while j >= 1:
#         print(j, end = ' ')
#         j -= 1
#     print()
#     i -= 1

# Bài 2.16
# n = 5 
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print("*", end = ' ')
#         j += 1
#     print()
#     i += 1
# n = 4
# i = n 
# while i >= 1:
#     j = i
#     while j >= 1:
#         print("*", end = ' ')
#         j -= 1
#     print()
#     i -= 1






    











