#bai 2.1 
# import math 
# x = int(input())
# y = int(input())
# z = int(input())
# p = (x + y + z)/2
# if(x+y > z and x+z > y and y+z > x):
#     print("là ba cạnh của tam giác" ,math.sqrt(p*(p-x)*(p-y)*(p-z)))
#     if(x==y and y!=z ):
#         print("S = " ,math.sqrt(p*(p-x)*(p-y)*(p-z) ))
#     elif(x==z and x!=y):
#         print("S = " ,math.sqrt(p*(p-x)*(p-y)*(p-z) ))
#     elif(y==z and y!=x):
#         print("S = " ,math.sqrt(p*(p-x)*(p-y)*(p-z) ))
#     elif(x==y and y==z and x==z):
#         print("S = " ,math.sqrt(p*(p-x)*(p-y)*(p-z) ))         
#     elif(x*x + y*y == z*z):
#         print ("S=" , x*y/2)
#     elif(x*x + z*z == y*y):
#         print("S=" , x*z/2)    
#     elif(y*y + z*z == x*x):
#         print("S=" , y*z/2)   


#bai 2.2
# n = int(input("nhập số"))
# if (n == 2):
#     print("Thứ hai")
# if (n == 3):
#     print("thứ ba")
# if (n == 4):
#     print("thứ tư")  
# if (n == 5):
#     print("thứ năm")
# if (n == 6):
#     print("thứ sáu")
# if (n == 7):
#     print("thứ bảy")
# if (n == 8):
#     print("chủ nhật")
# if(n == 1 or n == 9 or n ==10):
#     print("Không là ngày trong tuần")                          

#bai2.3
# n = int(input())
# if(n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12 ):
#     print("là tháng" , n , "có 31 ngày")
# if(n ==2):
#     print("là tháng" , n , "có 28 hoặc 29 ngày")
# if(n == 4 or n == 6 or n == 9 or n == 11):
#     print("là tháng" , n , "có 30 ngày")        
 
#bai2.4
# n = int(input())
# if(1 <= n <= 3 ):
#     print("mùa xuân")
# elif(n <= 6):
#     print("mùa hè")
# elif(n <= 9):
#     print("mùa thu")
# elif(n <= 12):
#     print("mùa đông")
# else:
#     print("mời nhập lại")                

#bai2.5
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# max = 1
# if(a > max):
#     max = a
# if(b > max):
#     max = b
# if(c > max):
#     max = c
# if(d > max):
#     max = d 
# print("số lớn nhất là :" , max)           
 
#bai2.6
# n = int(input())
# if( n == 1):
#     print("5000d")
# elif(n <= 5):
#     print((n-1)*4500+5000)
# elif(n <= 120):
#     print((n-5)*3500+4500*4+5000)
# elif(n > 120):
#     print(((n - 5)*3500+4500*4+5000)*1/10)            

#bai2.7
# h = int(input("Nhập số giờ : "))
# t = int(input("Nhập khung giờ : "))
# if(t >= 0 and t <= 7):
#     if (h == 7):
#         tien = h * 5000 * 300 * 60
#         print("số tiền là: ",tien)
#     else:
#         tien = h * 5000 * 300
#         print("số tiền là: ",tien)
# elif(t > 7 and t <= 17):
#     if (h >= 6):
#         tien = (h * 5000 * 400 * 60)/ 0.1
#         print("số tiền là: ",tien) 
#     else:
#         tien =  h * 5000 * 400
#         print("số tiền là: ",tien)
# else:
#     if (h >= 4):
#         tien = (h * 5000 * 350 * 60)/0.12
#         print("số tiền là: ",tien)
#     else:
#         tien = h * 5000 * 350
#         print("số tiền là: ",tien)

#bai2.9
# a = int(input("Nhập số cần tính tổng: "))
# tong = 0
# while(a > 0):
#     chuSo = a % 10
#     tong += chuSo
#     a //= 10

# print("Tổng các chữ số là:",tong)

#bai 2_10
# a = int(input("Nhập số cần đảo: "))
# soDao = 0
# while(a > 0):
#     chuSo = a % 10
#     soDao = soDao * 10 + chuSo
#     a //= 10
# print("Số sau khi đảo là",soDao)

#bai 2_11
# n = 3
# i = 1
# while (i <= n):
#     j = 1
#     while j <= i:
#         print("*", end=' ')
#         j += 1
#     print()
#     i += 1

#bai 2_12
# n = 5
# i = 1
# while (i <= n):
#     j = 1
#     while j <= i:
#         print(j, end=' ')
#         j += 1
#     print()
#     i += 1

#bai 2_13
# a = int(input("Nhập số cần tính tổng: "))
# tong = 0
# i = 1
# while(i <= a):
#     tong += i
#     i = i + 1
# print("Tong la",tong)

#bai 2_14
# n = 5
# i = n
# while i >= 1:
#     j = i
#     while j >= 1:
#         print(j, end=' ')
#         j -= 1
#     print()
#     i -= 1

#bai 2_15
# a, b = 0, 1
# count = 20
# print(a, b, end=' ')

# while count > 2:
#     c = a + b
#     print(c, end=' ')
#     a, b = b, c
#     count -= 1

#bai 2_16
# n = 5
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print("*", end=' ')
#         j += 1
#     print()
#     i += 1
# n = 4
# i = n
# while i >= 1:
#     j = i
#     while j >= 1:
#         print("*", end=' ')
#         j -= 1
#     print()
#     i -= 1