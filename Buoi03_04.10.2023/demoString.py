
des = 'Hà Nội '
des2 ="mùa này vắng những cơn mưa"

str1 =des + des2
print(str1)

str2 = "It's important"
str3 = 'He said , "I agree !"'
str4 = 'This string \n multiple'
str5 = 'This is a \' in a string'

print(str5)

path = 'C:\\Program Files\\Google\\Chrome\\Application'

print(path)

print(str(90))
mesage = '''Độc lập,
        Tự do,
        Hạnh phúc'''

print(mesage)

s = 'Parrot'
print('A' in s)
print(s.upper())
print(s.lower())
print(s.replace('r', 'n'))

print(len(s))

print(str1.split(" "))

str2 ="1;2;3;4;5;6;7"
print(str2.split(";"))




# Bai 01 : 
Kiểm tra tính hợp lệ của mật khẩu (là một giá trị string). 
Mật khẩu hợp lệ nếu:
Có ít nhất 6 kí tự
Chứa ít nhất một chữ cái (a-z hoặc A-Z)
Chứa ít nhất một chữ số (0-9)

password = input("Nhập pasword")

if(len(password) < 6):
    print("Mật khẩu ko hợp lệ")
    exit()
# check chu HOA
flag_chu_hoa = False
for x in password:
    X = x.upper()
    if(X >= 'A' and X <= 'Z'):
        flag_chu_hoa = True
        break

if not flag_chu_hoa:
    print("Mật khẩu cần chứa ít nhất 1 chữ cái (a-z/A-Z)")
    exit()

# check chu so
flag_chu_so = False
for x in password:
    if(x >= '0' and x <= '9'):
        flag_chu_so = True
        break

if not flag_chu_so:
    print("Mật khẩu cần chứa ít nhất 1 chữ số (0-9)")
    exit()

print('Mật khẩu hợp lệ')