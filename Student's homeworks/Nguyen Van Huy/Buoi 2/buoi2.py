# #bai 2.1
# import math
# a= int(input("canh a=  "))
# b= int(input("canh b=  "))
# c= int(input("canh c=  "))
# if((a==b and a==c) and (a==b and b==c) and (a==c and b==c)):
#     p=(a+b+c)/2
#     s=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print("tam giac nay la tam giac can co dien tich", s)
# elif(a==b and a==c and b==c ):
#     p=(a+b+c)/2
#     s=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print("tam giac nay la tam giac deu co dien tich", s)
# elif(a+b>c and b+c>a):
#     p=(a+b+c)/2
#     s=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print("tam giac nay la tam giac can co dien tich", s)
# elif(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
#     p=(a+b+c)/2
#     s=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print("tam giac nay la tam giac vuong", s)
# else:
#     print("khong phai la tam giac")

#bai 2.2
# a= int(input("Nhap mot so bat kì "))
# if(2<=a and a<= 7):
#     print("thu", a)
# elif(a==8):
#     print("thu",a)
# else:
#     print("khong phai ngay trong tuan")

#Bai 2.3
# a= int(input("Nhap mot thang bat ki:  "))
# if(a%2!= 0 and a<8):
#     print("Thang", a , "co 31 ngay")
# elif(a==2):
#     print("Thang", a , "co 28 ngay hoac 29 ngay")
# elif(a==4 or a==6):
#     print("Thang", a , "co 30 ngay")
# elif(a==8 or a== 10 and a==12):
#     print("Thang", a , "co 31 ngay")
# elif(a==9 or a==11):
#     print("Thang", a , "co 30 ngay")
# else:
#     print("Day khong phai la thang")

#Bai 2.4
# a = int(input("Nhap so thu nhat: "))
# b = int(input("Nhap so thu hai: "))
# c = int(input("Nhap so thu ba: "))
# d = int(input("Nhap so thu tu: "))
# if (a > b and a > c and a > d):
#     print("So lon nhat la", a)
# elif (b > a and b > c and b > d):
#     print("So lon nhat la", b)
# elif (c > a and c > b and c > d):
#     print("So lon nhat la", c)
# else:
#     print("So lon nhat la", d)

#Bai 2.5
# a = int(input("Nhập thang bat ki: "))
# if (a >= 1 and a <= 3):
#     print("Mua xuan")
# elif (a >= 4 and a <= 6):
#     print("Mua he")
# elif (a >= 7 and a <= 9):
#     print("Mua thu")
# elif (a >= 10 and a <= 12):
#     print("Mua dong")
# else: 
#     print("Day khong phai la thang")

#Bai 2.6
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
# tienvay = 400000000
# tientra = 10000000
# Thang = 1
# while(tientra < tienvay):
#     if(Thang<= 12):
#         Thang = Thang + 1
#         tienvay = tienvay - tientra
#     else:
#         Thang = Thang + 1
#         tienvay = tienvay + tienvay*(0.1/12) - tientra
# print(Thang)

#Bai 2.9
# a = int(input("Nhap so can tinh tong: "))
# tong = 0
# while(a > 0):
#     chuso = a % 10
#     tong = tong + chuso
#     a = a // 10
# print("Tổng các chữ số là:",tong)

#Bai 2.10
# a = int(input("Nhap so can dao: "))
# j=[]
# while(a > 0):
#     chuso = a % 10
#     j.append(str(chuso))
#     a = a // 10
# print("So duoc dao la:", "".join(j))

#Bai 2.11
# a=0
# c=int(input("nhap so dong: "))
# while(a<c):
#     print("*" * (a+1))
#     a+=1

#Bai 2.12
# n= int(input("Nhap so cuoi cung cua day so: "))
# i = 1
# while i <= n:
#     print(i * (i+1))
#     i += 1

# Bai 2.13
# n = int( input("So can nhap: "))
# tong=0
# a=1
# while(a<=n):
#     tong=tong+a
#     a+=1
# print(tong)

##Bai 2.15
# j=[]
# n=int(input("so luong chuoi so can in ra"))
# a = 0
# b = 1
# i = 0
# while i < n:
#     j.append(str(a))
#     next_term = a + b
#     a = b
#     b = next_term
#     i += 1
# print(",".join(j))

#Bai 2.16
# n=5
# i = 0
# a = 0
# while a < n:
#     print("* " * (a + 1))
#     a+=1
# while i < n:
#     print("* " * (n - i))
#     i+=1


