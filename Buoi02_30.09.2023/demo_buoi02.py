x = 6
A = (x > 7) or (x <6)
print(A)
#
#True or True  ==> True
#True or False ==> True
#False or True ==> True
#False or False ==> False

y = 10
B = (y > 10) and (y < 9)
print(B)


# True and True ==> True
# False and True ==> False
# True and False ==> False
# False and False ==> False

C = True
D = not C
print(D)


# a = int(input("Nhập số tự nhiên bất kỳ a = "))

# if( a%2 == 0):
#     print("a là số chẵn")
# if( a%2 != 0):
#     print("a là số lẻ")

# if(a%2 ==0):
#     print("a là số chẵn")
# else:
#     print("a là số lẻ")

# month = int(input("Nhập tháng trong năm month = "))

# if(month >=1 and month <=3):
#     print("Mùa xuân")
# elif(month >=4 and month <=6):
#     print("Mùa hạ")
# elif(month >=7 and month <= 9):
#     print("Mùa thu")
# elif(month >=10 and month <=12):
#     print("Mùa đông")
# else:
#     print("Không phải các tháng trong năm")
# n = 0
# while(n < 5):
#     print("n = ", n)
#     n = n + 1

n = 0
s = ""
while(n<100):
    if(n%3 ==0):
        # print(n, " ")
        s = s + str(n) + " "
    n = n + 1  
print(s)
  