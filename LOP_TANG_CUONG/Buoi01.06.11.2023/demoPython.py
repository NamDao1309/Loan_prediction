print("Hello World")
a = 32
print(type(a))
b = 3.9
print(type(b))
c = True
print(type(c))

d = "Ha Noi"
print(type(d))

e = "496"
f = int("496")
print(type(f))

x = None
y = x is None
print(y)

# Quy tac dat ten
#1. Ko duoc dat ten trung voi tu khoa : class, return, def, ...
#2. Ten ko duoc bat dau bang so
name, sex = "Peter", 1
print(f'Name : {name}\n Sex :{sex}')

# a  = int(input("Nhap a = "))
# if(a > 8):
#     print("a lon hon 8")
# elif(a < 20):
#     print(" a nho hon 20")
# else:
#     print("a lon hon 20")

# a  = int(input("Nhap a = "))
# if ( a % 2 == 0):
#     print("a la so chan")
# else:
#     print("a la so le")

# import math

# a = float(input("Nhap a = "))
# b = float(input("Nhap b = "))
# c = float(input("Nhap c = "))
# if( (a + b > c) and (b + c > a) and (c + a > b) ):
#     p = (a + b + c)/2
#     s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print("Dien tich tam giac la :" , s)
# else:
#     print("Khong phai la 3 canh tam giac")

# a = 0
# while(a < 5):
#     print(a)
#     a = a + 1

# n = float(input("Nhap n = "))
# i = 0
# sum_chan = 0
# sum_le = 0
# while(i <= n):
#     if ( i% 2 == 0):
#         sum_chan = sum_chan + i
#     else:
#         sum_le = sum_le + i
#     i = i + 1

# print("Tong cac so chan sum_chan = ", sum_chan )
# print("Tong cac so le sum_le = ", sum_le )

# n = float(input("Nhap n = "))
# i = 1
# while(i < n):
#     print(i)
#     if( i % 5 == 0):
#         #break
#         continue
#     i = i + 1

fruitList = [ "Apple", "Banana", "Mango","Kiwi", "Tomato" ]
for x in fruitList:
    print(x)


numerList = [1, 3, 5, 7, 9]
sum = 0
for y in numerList:
    sum = sum + y

print("Sum = ", sum)