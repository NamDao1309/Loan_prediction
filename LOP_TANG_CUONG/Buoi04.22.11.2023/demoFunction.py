import math

# def calculate_area_circle(r):
#     return math.pi*r*r

# r = 10
# print("Diện tích hình tròn với r = {0} là {1}".format(r, calculate_area_circle(r)))


# def max_2_so(a, b):
#     if(a> b):
#         return a
#     else:
#         return b

# a = float(input("Nhap a = "))  
# b = float(input("Nhap b = "))  
# print("Max 2 so({0}, {1}) la {2}".format(a, b, max(a,b)))

# def sum(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def multi(a, b):
#     return a * b

# def div(a, b):
#     """
#     Function tính thương 2 số
#     """
#     if(b != 0):
#         return a/b
#     else:
#         print("Không thực hiện được phép chia cho 0")


# def operation(x):
#     '''
#     Function check toán tử 2 số
#     '''
#     if(x.lower() == "+"):
#         print("Tổng ({0}, {1}) là: {2}".format(a, b, sum(a, b)))
#     elif(x.lower() == "-"):
#         print("Hiệu ({0}, {1}) là: {2}".format(a, b, sub(a, b)))
#     elif(x.lower() == "*"):
#         print("Tích ({0}, {1}) là: {2}".format(a, b, multi(a, b)))
#     elif(x.lower() == "/"):
#         print("Thương ({0}, {1}) là: {2}".format(a, b, div(a, b)))
#     else:
#         print("Không có toán tử nào được thực hiện")

# if __name__ == "__main__":
#     a  = float(input("Nhập a = "))
#     b  = float(input("Nhập b = "))
#     x = input("Nhập toán tử :")
#     operation(x)
#     print(operation.__doc__)

# lst = [3, 12, 7]

# def modify(k):
#     k.append(35)
#     print("k = ", k)

# print(" List ban đầu : ", lst)
# modify(lst)
# print(" List sau  : ", lst)

# x = 5
# def sum(a):
#     a = a + 10
#     print("a = ", a)

# print("x ban đầu  = ", x)
# sum(x)
# print("x sau  = ", x)


# def display(message, style='-'):
#     line = style * len(message)
#     print(line)
#     print(message)
#     print(line)

# display("Hello")
# display("Good morning", "*")
# display("Good morning", style = "/")
# display(style = "+", message = "Good arternoon")
# display(message = "Good evening")

a = float(input("Nhap a = "))
b = float(input("Nhap b = "))
try:
    thuong = a/b
    print("Thuong :", thuong)
except ZeroDivisionError:
    print("Khong thuc hien phep chia cho 0")
finally:
    print("Ket thuc tinh thuong 2 so")

