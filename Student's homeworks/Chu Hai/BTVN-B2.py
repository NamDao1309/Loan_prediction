# Bài 2.1
# import math
#  Nhập ba cạnh của tam giác từ người dùng
# a = float(input("Nhập độ dài cạnh a: "))
# b = float(input("Nhập độ dài cạnh b: "))
# c = float(input("Nhập độ dài cạnh c: "))
# # Tính nửa chu vi (p)
# p = (a + b + c) / 2

# # Tính diện tích của tam giác dựa vào loại tam giác
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:  # Tam giác đều
#         print(" Đây là tam giác đều ")
#         S = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     elif a == b or a == c or b == c:  # Tam giác cân
#         print(" Đây là tam giác cân ")
#         S = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:  # Tam giác vuông
#         print(" Đây là tam giác vuông ")
#         S = (a * b) / 2
#     else:  # Tam giác thường
#         print(" Đây là tam giác thường ")
#         S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
#     print(f"Diện tích của tam giác là: {S}")
# else:
#     print("Ba cạnh này không phải là ba cạnh của một tam giác.")
##
#Bai 2.2
# Nhập vào 1 số bất kỳ từ bàn phím từ 0 đến 10
# Kiểm tra xem số đó có là ngày trong tuần không? 
# Ví dụ Số 2 ==> Thứ 2
 # Số 3 ==> Thứ 3
 # ...
 # Số 8 ==> Chủ Nhật
# Mặt khác không là ngày trong tuần
# n= int(input("mời nhập số từ 0 đến 10: "))
# if (n>=2) and (n<=8):
#     if n==2:
#      print("thứ 2")
#     elif n==3:
#      print("thứ 3")
#     elif n==4:
#      print("thứ 4")
#     elif n==5:
#      print("thứ 5")
#     elif n==6:
#      print("thứ 6")
#     elif n==7:
#      print("thứ 7")
#     elif n==8:
#      print("CN")
# else:
#     print("không là ngày trong tuần")
###################################
#bài 2.3
