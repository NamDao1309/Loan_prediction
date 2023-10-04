# x = 2
# A = (x > 3 ) or (x <6)
# print(A)

# # True or True ==> True
# # True or False ==> True
# # False or False ==> True
# # False or False ==> False

# # True and true ==> True
# # False and True ==> False
# # True and False ==> False
# # False and  False ==> False

# y = 10
# C = True
# D = not C
# print(D)

# if(x > 0) :
#     print('x la so duong')

# a = int(input('canh cua tam giac a = '))
# print(' canh cua tam giac :',a)
# b = int(input('canh cua tam giac b = '))
# print(' canh cua tam giac :',b)
# c = int(input('canh cua tam giac c = '))
# print(' canh cua tam giac :',c)
# if(a % 2 == 0) :
#     print('a la so chan')
# else :
#     print('a la so le')

# if( a%2 == 0):
#     print('a la so chan')
# if( a%2 != 0):
#     print('a la so le')

# if( a%2 ==0) :
#     print('a la so chan')
# else:
#     print(' a la so le')
# if( a == 1 ):
#     print('a la mua xuan')
# if( a == 4 ):
#     print('a la mua ha')
# else:
#     print(' a la mua thu va dong')

# month = int(input('Nhap thang trong nam month = '))

# if(month >=1 and month <=3) :
#     print('mua xuan')
# elif(month >=4 and month <=6) :
#     print('mua ha')
# elif(month >=7 and month <= 9) :
#     print('mua thu')
# elif(month >=10 and month <=12) :
#     print('mua dong')
# else:
#     print('khong phai cac thang trong')

# if( a+b > c and b+c > a and c+a > b ) :
#     print(' la tam giac')
# n = 0
# while n < 5:
#     print("n = ", n)
#     n = n + 1
    
n = 0
while( n < 100) :
    if( n%3 ==0):
        print(n, end=', ')
    n = n + 1
