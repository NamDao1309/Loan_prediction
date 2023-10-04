import math
a = int(input('canh cua tam giac a = '))
print(' canh cua tam giac :',a)
b = int(input('canh cua tam giac b = '))
print(' canh cua tam giac :',b)
c = int(input('canh cua tam giac c = '))
print(' canh cua tam giac :',c)
if(a + b) > c and (b + c) > a and (a + c) > b:
    p = (a+b+c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
    s = (a*b)/2
    if a == b and b == c:
        print('day la tam giac deu va co dien tich la:', S)
    elif a == b or a == c or b == c :
        print('day la tam giac can va co dien tich la:', S)    
    elif a**2 + b**2 == c**2 or  a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('day la tam giac vuong va co dien tich la:' , s)
    else:
        print('day la tam giac thuong va co dien tich la:', S)
else:
    print('day khong phai la 3 canh cua tam giac')    
# test lll
