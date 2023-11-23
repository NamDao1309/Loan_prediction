message = 'This is a pencil'
message1 = "This is a pencil"
print(message1)

message2 = "It's a good time"
message3 = 'I said "I gree"'
message4 ="""
    Hôm nay trời nắng chang chang
    Mèo con đi học chẳng mang thứ gì
    Chỉ mang 1 chiếc bút chì
"""

print(message4)

message5 = "This is a\" in a string"
print(message5)

path = "C:\\Users\\Albert\\Documents\\Spells"
print(path)

message6 = "Ha Noi la thu do VN"
print(message6[0])
print(message6[1])
print(message6[2: 6])
print(message6[2:])
print(message6[:8])
print(message6[-1])
print(message6[-2])

print("Ha Noi" in message6)
print("ha Noi"not in message6)

message7 = "Welcome to Python"
print(message7.upper())
print(message7.lower())
print(message7.split(" "))
print(message7.replace("Python", "Java"))

print(','.join(['Welcome', 'to', 'Python']))

name = 'Hoang Dao Thuy'
year = 28
height =  167
print("His name is %s" % name)
print("His year old is %d" % year)
print("His name is {0}. His year old is {1}".format(name, year) )
print("His name is {0}. His year old is {1}. His height is {2}".format(name, year, height) )

colorList = ['yellow', 'black', 'white', 'orange', 'green']
print(colorList[2])
print(colorList[-2])

colorList.reverse()
print(colorList)

colorList.sort()
print(colorList)

colorList.sort(reverse=True)
print(colorList)

colorList.append(12)
print(colorList)

numberList = [1, 3, 6, 9]
colorList.extend(numberList)
print(colorList)

colorList.remove(12)
print(colorList)

colorList.pop()
print(colorList)

colorList.clear()
print(colorList)

numbers = [1, 7, 98, 34]
del numbers

# countNumber = 0
# s = input("Nhap chuoi bat ky :")
# inputStr =s.split(" ")
# print(inputStr)
# for item in inputStr:
#     if(item.replace(".","").isnumeric()):
#         countNumber +=1

# print("So lan xuat hien so :",countNumber)

colors ={'blue':"màu xanh",'red': "màu đỏ", 'yellow':'màu vàng', 'green': 'màu xanh lá cây'}
for key in colors.keys():
    print(key)

for value in colors.values():
    print(value)    

for key,value in colors.items():
    print(key, " : ", value)