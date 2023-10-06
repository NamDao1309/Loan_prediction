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

