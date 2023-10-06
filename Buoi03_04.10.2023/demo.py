<<<<<<< HEAD
# i = 0
# while(i < 5):
#     print(i)
#     if (i == 3):
#         break
#     i = i + 1

#range (start, stop, step)
# start = 0 | step = 1 (default)

#ham range
# for i in range(0, 9, 1):
#     print(i)

# listFruit = ["Apple", "Banana", "Kiwi", "Mango"]
# for fruit in listFruit:
#     print(fruit)

#bai3_1
# for i in range(3, 300, 3):
#     print(i)

# count = 0
# for i in range (1, 100):
#     count += i
# print(count)
        
#in bảng cửu chương
# for i in range(1,10):
#     for j in range (1, 10):
#         print(i , "*", j, "=", i *j)
#     print()

#bai3
# danSo = 95500000
# tocDo = 0.012
# nam = 2017

# while(danSo < 150000000):
#     danSo = danSo * (1 + 0.012)
#     nam += 1 
# print("Năm đạt được 150 triệu người là", nam)


#chuyển đổi từ thập phân sang nhị phân
# x = int(input("Nhập vào số cần chuyển: "))
# s = ''
# while(x > 0):
#     i = x % 2
#     s = str(i) + s
#     x = x // 2
# print(s)

#String
# des = 'Hà Nội'
# des2 = "mùa này vắng những cơn mưa"
# str = des + ' ' + des2
# print(str)

# str2 = "It's important"
# str3 = 'He said , "I agree!"'
# str4 = "This string \n multiple"
# str5 = 'This is a \' in a string '

# print(str(90))
# message = '''Độc lập,
#             tự do,
#             hạnh phúc'''
# print(message)

#Bài toán kiểm tra tính hợp lệ của mật khẩu
password = input("Nhập mật khẩu: ")
length = len(password)
if (length < 6):
    print("Mật khẩu không hợp lệ")
    exit()
#check chu hoa
flag_chu_hoa = False
for x in password:
    X = x.upper()
    if (X >= 'A' and X <= 'Z'):
        flag_chu_hoa = True
        break
if not flag_chu_hoa:
    print("Mật khẩu cần chứa ít nhất một chữ cái (a-z/A-Z)")
    exit()

#check chữ số
flag_chu_so = False
for x in password:
    if (x >= '0' and x <= '9'):
        flag_chu_so = True
        break
if not flag_chu_so:
    print("Mật khẩu cần ít nhất một chữ số từ 0-9")
    exit()

print('Mật khẩu hợp lệ')

=======

# i = 0
# while(i<5):
#     i = i + 1
#     if(i == 3):
#         # break
#         continue
#     print(i)

# ham range
# Vong lap for cai tien
for x in range(6):
    print(x)

listFruit = ["Apple", "Banana", "Kiwi", "Mango"]

for y in listFruit:
    print(y)

# Bai 02: In Bang Cuu Chuong
for i in range(2,10):
    for j in range(2,10):
        print(i, '*', j, '=', i*j)
 
# Bai 03 : Dân số Việt Nam năm 2017 
# là 95.5 triệu người. Nếu tốc độ tăng dân số trung bình 
# năm là 1.2% thì đến năm bao nhiêu dân số Việt Nam 
# là 150 triệu
pop = 95.5
year = 2017
rate = 1.2/100

while(pop<150):
    year = year + 1
    pop = pop*(1 + rate)

print(" Năm dân số đạt 150tr là :", year)

# Bai 04: Chuyển một số từ hệ thập phân sang hệ nhị phân.

number = int(input("Nhap so bat kỳ :"))

s = ''
while(number >0):
    i = number%2
    s = str(i) + s
    number=int(number/2)

print(s)
>>>>>>> 8892f7767c50c0e4603a8ce086d30a2fb8d2aa74
