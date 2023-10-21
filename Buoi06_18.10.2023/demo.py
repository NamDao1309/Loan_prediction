#func tính diện tích
# import math
# def tinh_dien_tich_HCN(a, b):
#     """
#     Tính diện tích hcn
#     """
#     return a * b

# # a*x^2 + b*x + c = 0
# def giải_pt_bac_hai(a, b, c):
#     if(a == 0):
#         if(b == 0):
#             if(c == 0):
#                 print("Phương trình có vô số nghiệm")
#             else:
#                 print("Phương trình vô nghiệm")
#         else:
#             print("Phương trình có 1 nghiệm duy nhất: ", -c/b)
#     else:
#         delta = b*b - 4*a*c
#         if (delta < 0):
#             print("Phương trình vô nghiệm")
#         elif(delta == 0):
#             print("Phương trình có nghiệm kép:", -b/(2*a))
#         else:
#             x1 = (-b + math.sqrt(delta))/(2*a)
#             x2 = (-b - math.sqrt(delta))/ (2*a)
#             print("Phương trình có 2 nghiệm x1 =", x1, "và x2 =", x2)

# def kiem_tra_TG(a, b, c):
#     if (a + b > c and a + c > b and b + c > a):
#         if (a == b and a == c):
#             print("Đây là tam giác đều")
#         elif (a * a + b * b == c * c or b * b + a * a == c * c or b * b + c * c == a * a):
#             print("Đây là tam giác vuông")
#         elif (a == b or a == c or b == c):
#             print("Đây là tam giác cân")
#         else:
#             print("Đây là tam giác thường")
#     else:
#         print("Đây không phải là tam giác")

# if __name__ == '__main__':
# #call function
#     print(tinh_dien_tich_HCN(3, 4))

#     giải_pt_bac_hai(3, 10, 8.)

# #function kiểm tra tam giác

#     kiem_tra_TG(6, 6, 6.)

#     print(tinh_dien_tich_HCN.__doc__)

# #function có 2 cách truyền : truyền tham trị(giá trị)
# #                            truyền tham chiếu (truyền địa chỉ)

# a = 3
# b = 4
# tinh_dien_tich_HCN(a, b)

# #vd: truyền tham chiếu
# lst = ['Apple', 'Banana', 'Mango']
# def add_item(listFruit):
#     listFruit.append('Kiwi')
#     print("listFruit: " , listFruit)
# add_item(lst)
# print("After lst: ", lst)


def display(message, code = '+'):
    line = code * len(message)
    print(line)
    print(message)
    print(line)

display("Hello")

display("Goodbye", "*")

display("GoodNight", code = "*")

display(code = ".", message= "GoodMorning")

# def tinh_tong(a, b):
#     print("Tong: ", a + b)

# def tinh_tong(a, b, c):
#     print("Tổng = ", a + b + c)

def tinh_tong(*arg):
    s = 0
    for x in arg:
        s = s + x
    print("Tổng = ",s)

tinh_tong(4,6,7,8)

#hàm lamda
def cube(x): return x * x * x

print(cube(5))

cube_v2 = lambda x: x * x * x
print(cube_v2(6))

#function in function
def hien_thi():
    str1 = "Hà Nội"
    def hien_thi2(): 
        print(str1)
    hien_thi2()

hien_thi()

a = 1000
try:
    thuong = a/0
except ZeroDivisionError:
    print("ZeroDivisionError occured")
