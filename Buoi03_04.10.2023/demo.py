
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