import math
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


# bài toán tam giác
# a = int(input("Nhập a = "))
# b = int(input("Nhập b = "))
# c = int(input("Nhập c = "))
# if (a + b) > c and (b + c) > a and (a + c) > b:
#     if a == b == c:
#         print("Đây là tam giác đều")

#     elif a == b or a == c or b == c:
#         print("Đây là tam giác cân")

#     elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         print("Đây là tam giác vuông")
    
#     else:
#         print("Đây là tam giác thường")

# else:
#     print("Đây không phải là 3 cạnh của tam giác")

s = ""
n = 0
while(n < 100):
    if (n % 3 == 0):
        s = s + str(n) + " "
    n = n + 1
print(s)