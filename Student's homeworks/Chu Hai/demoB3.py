#bài tập vòng lặp while
#sự khác nhau giữa break và continue

# i= 0
# while(i<5):
#     if(i==3):
#         break
#     i=i+1
#     print(i)
#hamf range
# for x in range(9):
#     print(x)
# tổng số nguyên 1-100 sử dụng for/range
# S=0
# for i in range(1,101,):
#  S += i
#  print(S)


########### in ra bảng cửu chương
# for i in range(1, 10):
#     for j in range(1, 10):
#         F = i * j
#         print(f"{i} x {j} = {F}")
#     print() 
# dân số vn 2017 là 95,5tr ng , tốc độ tăng hằng năm là 1,2% thì đến năm bao nhiêu đạt 150 tr người
# sonam = 2017  # Khởi tạo số năm
# hientai= 95.5
# datden=150
# tocdo=0.012

# while hientai < datden:
#      hientai = hientai*(1 + tocdo)
#      sonam += 1

# print(f"Dân số Việt Nam sẽ đạt 150 triệu người vào {sonam} ")
# def to_binary(n):
#   """
################  Chuyển đổi số thập phân sang hệ nhị phân

#   Args:
#     n: Số thập phân cần chuyển đổi

#   Returns:
#     Số nhị phân của n
#   """

#   if n == 0:
#     return "0"

#   return "1" + to_binary(n // 2) if n % 2 else to_binary(n // 2)


# def main():
#   # Nhập số thập phân cần chuyển đổi
#   n = int(input("Nhập số thập phân cần chuyển đổi: "))

#   # Chuyển đổi sang hệ nhị phân
#   binary_number = to_binary(n)

#   # In kết quả
#   print("Số nhị phân của {} là: {}".format(n, binary_number))


# if __name__ == "__main__":
#   main()
  #cách 2
  # Nhập số nguyên từ người dùng
"""songuyen = int(input("Nhập số nguyên: "))

# Chuyển đổi sang hệ nhị phân và lưu vào biến nhi_phan
nhiphan = bin(so_nguyen)

# Lấy chuỗi nhị phân từ kết quả và loại bỏ các ký tự '0b' ở đầu
chuoinhiphan = nhiphan[2:]

print(f"Số {songuyen} trong hệ nhị phân là: {chuoinhiphan}")
"""
#cách 3
"""# Nhập số nguyên từ người dùng55
so_nguyen = int(input("Nhập số nguyên: "))

# Khởi tạo biến lưu chuỗi nhị phân
chuoi_nhi_phan = ""

# Chuyển đổi số nguyên sang hệ nhị phân
while so_nguyen > 0:
    chuoi_nhi_phan = str(so_nguyen % 2) + chuoi_nhi_phan
    so_nguyen = so_nguyen // 2

print(f"Số đã nhập trong hệ nhị phân là: {chuoi_nhi_phan}") """


################### kiểm tra tính hợp lệ của một mật khẩu( giá trị string)
#mật khẩu hợp lệ nếu có ít nhất 6 ký tự, chứa ít nhất một chữ cái (a-z) or(A-Z), có chứa một chữ số(0-9)

import re

def is_valid_password(password):
    if len(password) < 6:
        return False
    
    if not re.search("[a-zA-Z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    return True  

while True:
    password = input("Nhập mật khẩu: ")
    if is_valid_password(password):
        print("Mật khẩu hợp lệ.")
        break  # Thoát khỏi vòng lặp khi mật khẩu hợp lệ
    else:
        print("Mật khẩu không hợp lệ. Vui lòng nhập lại.")
