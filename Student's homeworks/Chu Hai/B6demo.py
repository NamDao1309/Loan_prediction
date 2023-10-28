import math
# tính diện tích
def tinh_S_HCN(a,b):
    return a*b

#a*x2 +b*x +c=0
import math

# def bachai(a, b, c):
#      '''
#         có chức năng tính bậc hai
#         '''
#     # Tính delta
# delta =(b**2 - 4*a*c)
#     # Kiểm tra giá trị của delta
# if delta > 0:
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         return "Phương trình có hai nghiệm phân biệt:", x1, x2
# elif delta == 0:
#         x = -b / (2*a)
#         return "Phương trình có một nghiệm kép:", x
# else:
#         return "Phương trình vô nghiệm"
#     #  if(a==0):
    #       if(b==0):
    #            if(c==0):
    #                 print("phuong trinh vo số nghiệm")
               
    #         print("phuong trinh có nghiệm duy nhất x=:",-c/b)
    # # else:
    #     delta=( b*b - 4*a*c)
    #     if(delta<0):
    #          print("phuong trinh vô nghiệm")
    #     if(delta==0):
    #          print("phuong trinh có nghiệm kép ", -b/(2*a))
    #     else:
    #  x1 = (-b - math.sprt(delta))/(2*a)
    #  x2 = (-b + math.sprt(delta))/(2*a)
    # print("phuong trinh có nghiệm x1, x2 = ", x1, x2)
# gọi funtion
# a = int(input("nhập vào số a bất kỳ"))
# b = int(input("nhập vào số b bất kỳ"))
# c = int(input("nhập vào số c bất kỳ"))
#  Bachai= phuongtrinhbachai(a,b,c)


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

# if __name__=='__main__':
#     bachai(1,2,-1)
#     print(bachai,__doc__)

    #########################################
    #hàm lamda
def cube(x): return x*x*x
print(cube(4))
# finally:
cubev2= lambda x : x*x*x
print(cubev2(6))
   
# dùng bỏ qua lỗi
a=1000
try:
     thuong=a/0
except ZeroDivisionError:
     print("zero OK")

def func(a):
     if(a<4):
        b= a/(a-3)
        print("gia tri b:",b)
try:
     func(3)
     func(5)
except ZeroDivisionError:
    print("lỗi Ok")
except NameError:
    print("lỗi tên")