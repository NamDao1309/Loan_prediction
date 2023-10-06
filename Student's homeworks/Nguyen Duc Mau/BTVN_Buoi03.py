import math
#bai 3_1
# for i in range(3, 300, 3):
#     print(i)

#bai 3_2
# s = input("Nhập chuỗi s: ")
# count = 0
# for x in s:
#     if (x >= '0' and x <= '9'):
#         count += 1
# print(count)

#bai 3_3
# s = input("Nhập chuỗi s: ")
# tachS = s.split()
# chuoiSauKhiTach = "\n".join(tachS)
# print(chuoiSauKhiTach)

#bai 3_4
# a = int(input("Nhập số cần kiểm tra: "))
# i = int(math.sqrt(a))
# if (i * i == a):
#     print("Đây là số nguyên tố")
# else:
#     print("Đây không phải là số nguyên tố")

#bai3_5
# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))
# while b:
#     a, b = b, a % b
# print("Ước chung lớn nhất là", a)

#bai 3_6
# N = int(input("Nhập N: "))
# sum = 0
# for i in range(N + 1):
#     sum += i
# print(sum)

#bai 3_7
# N = int(input("Nhập N: "))

# def soNT(N):
#     count = 0
#     if N < 2:
#         return False
#     for i in range(2, int(N**0.5) + 1):
#         if (N % i == 0):
#             count += 1

#     return count == 0
# sum = 0
# for j in range(2, N):
#     if soNT(j):
#         sum += j    

# print("Tổng các số nguyên tố là:", sum)

#bai 3_10
#in bảng cửu chương
# for i in range(1,10):
#     for j in range (1, 10):
#         print(i , "*", j, "=", i *j)
#     print()

#bai 3_8
N = int(input("Nhập N: "))

def soNT(N):
    count = 0
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if (N % i == 0):
            count += 1

    return count == 0
tong = 0
dem = 0
number = 2
while dem < N:
    if soNT(number):
        tong += number
        dem += 1
    number += 1

print("Tổng các số nguyên tố nhỏ hơn N là:", tong)