# viết chương trình nhập vào một tháng ra mùa của tháng đó
#mm = int(input("Nhập vào một tháng bất kỳ trong năm: "))

#if (mm == 1 or mm == 2 or mm == 3):
#    print("Mùa xuân")
#else:
#    if (mm == 4 or mm == 5 or mm == 6):
#        print("Mùa hạ")
#    else:
#        if (mm == 7 or mm == 8 or mm == 9):
#            print("Mùa thu")
#        else:
#            if (mm == 10 or mm == 11 or mm == 12):
#                print ("Mùa đông")

# if (mm >= 1 and mm <=3):
#     print("Mùa xuân")
# else:
#     if (mm >= 4 and mm <=6):
#         print("Mùa hạ")
#     else:
#         if (mm>=7 and mm<=9):
#             print("Mùa thu")
#         else:
#             if (mm>=10 and mm<=12):
#                 print("Mùa đông")
#             else:
#                 print("Không phải các tháng trong năm")


#Nhập vào ba số kiểm tra có phải của một tam giác không
# import math
# a = float(input("Nhập chiều dài cạnh thứ nhất "))
# b = float(input("Nhập chiều dài cạnh thứ hai "))
# c = float(input("Nhập chiều dài cạnh thứ ba "))
# t1 = a**2 + b**2 - c**2
# t2 = a**2 + c**2 - b**2
# t3 = c**2 + b**2 - a**2
# p=(a+b+c)/2
# if (a+b>c and a+c>b and b+c>a):
#     if (t1 == 0):
#         S = a*b/2
#     elif (t2 == 0):
#         S = a*c/2
#     elif (t3 == 0):
#         S=b*c/2
#     else:
#         S = math.sqrt((p-a)*(p-b)*(p-c))
#     print("Diện tích tam giác: ",S)
# else:
#     print("Không phải tam giác")   
 


#In các số chia hết cho 3 từ 1 đến 100
# z = 1
# s=""
# while (z<=100):
#     if(z%3==0):
#         #print(z," ")
#         s = s + str(z) + " "
#     z = z +1

# print(s)


# đáp án btap về nhà
print("Đáp án bài số 2: C - C - B - B - A - C - B - C")

#bài 2.1
import math

a = float(input("nhập cạnh thứ nhất: "))
b = float(input("Nhập cạnh thứ hai: "))
c = float(input("Nhập cạnh thứ ba: "))
if (a<b+c and b<a+c and c<b+a):
    if a**2 == b**2 + c**2:
        print("S = ", b*c/2)
    if b**2 == a**2 + c**2:
        print("S = ", a*c/2)
    if c**2 == a**2 + b**2:
        print("S = ", a*b/2)
    p = (a+b+c)/2
    S = math.sqrt((p-a)*(p-b)*(p-c))
    print("S = ",S)
print("ko phải là tam giác")