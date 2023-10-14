txt = "Welcom to Python for EveryBody"
print("Python" in txt)
print("Python" not in txt)
print(txt.upper())
print(txt.lower())
print(txt.split(' '))
print(txt.replace('Python', 'Java'))

#String Format
print("I get {0} math point and {1} Literature point".format(8.23,8.3))

name = "Drake"
age = 22
x = 'D'
print(f"Hello, my name is {name}. I'm {age} years old") #phải có 'f' ở đầu để định dạng lại
print("ký tự %c "%(x))
print('họ và tên: %s' %('Hoàng Hoa Thám'))

print("số tự nhiên: %d %i %u" %(10,3,5.7))
print("số octal: %o" %(30))


#--------------------------------------

#list phải là []
listfruit = ["orange","mango","watermelon","apple"]
print(listfruit)

listnumber = [3,-9.4,4,923.1,23]
print(listnumber)

list_Item = [ 'Apple', True, 3.6, 'B', ['math', 'physic', 'chemistry']]
print(list_Item)
print(list_Item[3])
print(list_Item[4][1])

print(list_Item[-1][-3]) # truy suất ngược [-3,-2,-1]

# Slicing
print(list_Item[1:4])
print(list_Item[:4])

print(list_Item[3:])

print(True in list_Item)
print(True not in list_Item)

#Lấy độ dài
print(len(list_Item))

# Đảo ngược list
list_Item[4].reverse()
list_Item.reverse()
print(list_Item)

# Sap xep 
listnumber.sort()
#listnumber.sort(reverse=True)
print(listnumber)

# add agent
listnumber.append(6)
listnumber.append(6)
listnumber.append(6)
print(listnumber)

# Delete item
listnumber.remove(6)
print(listnumber)

# Get item with position 
print(listnumber.pop(3))
print(listnumber.pop()) # get first item in stack

listFloat = [4.5,8.3,9.2,11.2]

# Hợp 2 list thành 1
listnumber.extend(listFloat)
print(listnumber)

# Xóa tất cả phần tử
# listnumber.clear()
# print(listnumber)

# Hủy 1 List
# del listnumber
# print(listnumber)

# Copy List
# Cách 1
listnumber2 = listnumber
print(listnumber2)

# Cách 2: dùng hàm copy
listnumber3 = listnumber.copy()
print(listnumber3)


# Dem so phan tu xuat hien
print(listnumber.count(6))
print(list_Item[0].count('math'))

# Lay chi so index cua phan tu
print(listnumber.index(3))

# insert mot phan tu vao vi tri nao do
listnumber.insert(3, 'Ha Noi')
print(listnumber)

# Hop 2 list
lst = listnumber2 + [1,2,3,4]
print(lst)

#Bai 4.4
nm1=int(input('Nhap so bat ky tu 0-99 '))
S = ""
if (nm1>=0 and nm1 <=99):
    string1 = str(nm1)
    for i in range(0,2):
        if string1[1] == '0' and string1[0] == '0':
            S = S + "khong"
        if string1[0] == '1':
            S = S + "muoi "
        if string1[i] == '2':
            S = S + "hai "
        if string1[i] == '3': 
            S = S + "ba "
        if string1[i] == '4':
            S = S + "bon "
        if string1[i] == '5':
            S = S + "nam "
        if string1[i] == '6':
            S= S + "sau "
        if string1[i] == '7':
            S = S + "bay "
        if string1[i] == '8':
            S = S + "tam "
        if string1[i] == '9':
            S = S + "chin "
        if i == 0 and string1[i] not in [0,1]:
            S = S + "muoi "
        print(string1[i])
print(S)

# kieu tuple : mot tap gia tri khong the thay doi duoc
tupleNumber = (1,9,8)
listNumber4 = list(tupleNumber)
listNumber4.append(4)
tupleNumber = tuple(listNumber4)