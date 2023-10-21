import math

# Func tinh dien tich
def tinh_dien_tich_HCN(a, b):
    """
    Tính diện tích hình chữ nhật
    """
    return a*b


# a*x2+ b*x+c = 0
def giai_pt_bac_hai(a, b, c):
    '''
    Function có chức năng giải phương trình bậc 2
    '''
    if(a==0):
        if(b==0):
            if(c==0):
                print("Phuong trinh Vo So Nghiem")
            else:
                print("Phuong trinh vo nghiem")
        else:
            print("Phuong trinh co nghiem duy nhat :",-c/b)
    else:
        delta = b*b - 4*a*c
        if(delta<0):
            print("Phuong trinh vo nghiem")
        elif(delta == 0):
            print("Phuong trinh co nghiem kep x1 = x1 = " ,-b/ (2*a) );
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print("Phuong trinh co 2 nghiem phan biet x1 = ", x1, " va x2 = ", x2)



# if __name__ == '__main__':
#     # call function
#     print("Dien tich HCN la :", tinh_dien_tich_HCN(3,4))

#     giai_pt_bac_hai(1,-2,1)
#     print(giai_pt_bac_hai.__doc__)
#     print(tinh_dien_tich_HCN.__doc__)


# function có 2 cách truyền : truyền tham trị ( giá trị )
#                             truyền tham chiếu ( truyền địa chỉ )


# VD : truyền tham trị
a = 3
b = 4
tinh_dien_tich_HCN(a, b)
print(a)
print(b)

# VD : Truyền tham chiếu
lst = ["Apple", "Banana", "Mango"]
print("Before lst :" , lst)

def add_item(listFruit):
    listFruit.append('Kiwi')
    print("listFruit :" , listFruit)


add_item(lst)

print("After lst :" , lst)


def display(message, code ='+'):
    line = code * len(message)
    print(line)
    print(message)
    print(line)

display("Hello")

display("Goodbye", "*")

display("GoodNight", code="*")

display(code = ".",message = "GoodMorning")

def tinh_tong(a, b):
    print("Tong :", a+b)

def tinh_tong(a, b, c):
    print("Tong :", a+b+c)

def tinh_tong(*arg):
    s = 0
    for x in arg:
        s = s + x
    print("Tong :", s)


# tinh_tong(6, 7)
tinh_tong(6, 7, 8, 9, 10, 11, 12, 13)

# Hàm lamda
def cube(x): return x*x*x

print(cube(5))

cube_v2 = lambda x : x*x*x
print(cube_v2(6))

# Function in Function
def hien_thi():
    str1 = "Ha Noi"
    def hien_thi2():
        print(str1)
    hien_thi2()

hien_thi()

# a = 1000
# try:
#     thuong = a/ 0
# except ZeroDivisionError:
#     print("ZeroDivisionError occured ")



def func(a):
    if(a<4):
        b = a/(a-3)
    print("Value of b = ", b)

try:
    func(3)
    func(5)
except ZeroDivisionError:
    print("ZeroDivisionError occured")
except NameError:
    print("NameError occured")
