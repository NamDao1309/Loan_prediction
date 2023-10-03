 # in dữ liệu 

#true and true=>> true
# true and false ==> false
#fales and true ->> false
# false and false=> false
 
#a = int(input("nhap so bat ky a= "))
# Nhập một số từ người dùng
# Sử dụng toán tử modulo (%) để kiểm tra số chẵn hay lẻ
#if a % 2 == 0:
 #   print("{a} là số chẵn")
#if(a%2 != 0):
 #   print("{a} là số lẻ")
# Nhập tháng từ người dùng
# thang = int(input("Nhập một tháng (1-12): "))
# if (thang >= 1 and thang <= 3):
#     print("mua xuân")
# elif(thang>=4 and thang <=6):
#     print("mua hạ")
# elif(thang>=7 and thang<=9):
#     print = ("Mùa thu")
# elif(thang>=10 and thang<=12):
#     print = ("Mùa đông")
# else:
#     print("Tháng không hợp lệ. Vui lòng nhập từ 1 đến 12.")
# Nhập tháng từ người dùng
# thang = int(input("Nhập một tháng (1-12): "))

# # Sử dụng câu lệnh if-elif-else để xác định mùa
# if thang >= 1 and thang <= 12:
#     if thang in [12, 1, 2]:
#         mua = "Mùa Đông"
#     elif thang in [3, 4, 5]:
#         mua = "Mùa Xuân"
#     elif thang in [6, 7, 8]:
#         mua = "Mùa Hạ"
#     else:
#         mua = "Mùa Thu"
    
#     print(f"Tháng {thang} thuộc mùa {mua}")
# else:
#     print("Tháng không hợp lệ. Vui lòng nhập từ 1 đến 12.")

# BÀi 3 : kiểm tra xem có phải tam giác không và tính diện tích
# a = float(input("Nhập độ dài cạnh a: "))
# b = float(input("Nhập độ dài cạnh b: "))
# c = float(input("Nhập độ dài cạnh c: "))

# # Kiểm tra điều kiện tam giác
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("Đây là tam giác đều")
#     elif a == b or a == c or b == c:
#         print("Đây là tam giác cân")
#     elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         print("Đây là tam giác vuông")
#     else:
#         print("Đây là tam giác thường")
# else:
#     print("Ba số này không phải là ba cạnh của một tam giác.")
# demo bài vòng lặp while
n=1
s= ""
while(n<=100):
    if(n % 3 == 0):
      #print("n= ",n)
      s= s + str(n)+ " "
    n = n + 3
print(s)