# #bai3.1
# for i in range(3,300,3):
#     print(i)

# bai3.10
# for i in range(2,10):
#     for j in range(1,10):
#         s = i * j
#         print(i , '*' , j , '=' , s)
#     print()  

#bai3.6
# n = int(input())
# tong = 0
# for i in range(n):
#     so_nguyen = int(input("Nhập số nguyên thứ {i + 1}: "))
#     tong += so_nguyen
# print(tong)

#bai3.4

n = int(input("nhập số"))
if (n < 2):
    print("không là số nguyên tố!")
for i in range(2,int(n**0.5)+1):
    if(n % i != 0):
        print("là số nguyên tố!")
    else:        
        print("không là số nguyên tố!") 
               
