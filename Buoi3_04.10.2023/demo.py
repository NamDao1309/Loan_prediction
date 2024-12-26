# i = 0 
# while(i<5):
#     i = i + 1
#     if(i == 3):
#         continue
#     print(i)  
    
#ham range
# for i in range(1,5,1):
#     print(i)

# listFruit = ["apple" , "orange" , "banana" ]
# for y in listFruit :
#     print(y)

# for i in range(3,300,3):
#     print(i)

# sum = 0
# for i in range(1,101,1):
#     sum += i 
# print(sum)   

#in bang cuu chuong

# for i in range(2,10):
#     for j in range(1,10):
#         s = i * j
#         print(i ,'*' ,j , '=' ,s)  
#     print()

#tinh dan so

# danso = 95.5
# sonam = 2017
# tanghangnam = 0


# while danso < 150 :
#     danso = danso*(1+0.012)
#     sonam += 1
# print(sonam)    



# #chuyển 1 số từ hệ thập phân sang nhị phân

# number = int(input("nhập số:"))
# s = ''
# while (number > 0 ):
#     i = number%2
#     s = str(i) + s
#     number = int(number/2)
# print(s)    

# des = 'Hà Nội'
# des1 = "màu này vắng những cơn mưa"

# str = des + des1
# print(str)

# str2 = "it's important"
# str3 = 'he said , "I agree!"'
# str4 = 'this string \n multiple'
# str5 = 'This is a \'in a string'

# print(str(90))

#kiểm tra tính hợp lệ của mật khẩu
# password = str(input("nhập mật khẩu:"))
# if(len(password) < 6):
#     print("mật khẩu không hợp lệ")
#     exit()
# #check chu Hoa    
# flag_chu_hoa = False
# for x in password:
#     X = x.upper()
#     if(X >= 'A' and X <= 'Z'):
#         flag_chu_hoa = True
#         break
# if not flag_chu_hoa:
#     print("Mật khẩu cần chứa ít nhất 1 chữ cái")
#     exit()
# flag_chu_hoa = False
# for x in password:
#     if(x >= ' 0' and x <= '9'):
#         flag_chu_hoa = True
#         break
# if not flag_chu_hoa:
#     print("Mật khẩu cần chứa ít nhất 1 số")
#     exit()
# print("mật khẩu hợp lệ")            