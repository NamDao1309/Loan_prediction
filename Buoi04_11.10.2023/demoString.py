txt ="Welcome to Python For Everybody"
print("Python" in txt)
print("Python" not in txt)
print(txt.upper())
print(txt.lower()) 
print(txt.split(' '))
print(txt.replace('Python', "Java"))

# String Format
print("Tôi được {0} điểm Toán và {1} điểm Văn".format(8.5, 7.8))

name = "Tommy"
age = 26
x = 'A'
print(f"Xin chào, Tên tôi là {name}. Tôi {age} tuổi")
print('Ký tự %c' %(x))
print('họ và Tên : %s' %('Hoàng Hoa Thám'))

print("Số tự nhiên : %d %i %u" %(10, 3, 5.4))
print("Số octal : %o " %(36))

#-----------------------
listFruit = ['Lê', 'Thị', 'Mận', 'Đào']
print(listFruit)

listNumber =[3, 9, 2.5, -10]
print(listNumber)

listItem = ['Apple', True, 3.5, 'B', ["Toán", "Lý", "Hóa"]]
print(listItem)
print(listItem[2])
print(listItem[4][1])

print(listItem[-1][-3])
print(listItem[-1][0])

# Slicing
print(listItem[1:4])

print(listItem[:4])
print(listItem[3:])

print(listItem[:])

print(True in listItem)
print(True not in listItem)

# lay do dai 
print(len(listItem))

# dao nguoc list
listItem.reverse()
print(listItem)

# Sap xep
listNumber.sort() 
#listNumber.sort(reverse=True) 
print(listNumber)

# add number
listNumber.append(6)
listNumber.append(6)
print(listNumber)

# delete item
listNumber.remove(6)
print(listNumber)

# get item with position
print(listNumber.pop(3))
print(listNumber.pop())  # get item o dau stack

listFloat = [4.6, 2.9, 7.0, -5.8]

# Hop 2 list thanh 1
listNumber.extend(listFloat)
print(listNumber)

# Xoa tat ca phan tu
# listNumber.clear()
# print(listNumber)

# Huy 1 list
# del listNumber

# Copy List
# Cach 1
listNumber2 = listNumber
print(listNumber2)

# Cach 2 : dung ham copy()
listNumber3 = listNumber.copy()
print(listNumber3)

# Dem so phan tu xuat hien
print(listNumber.count(3))

# Lay chi so index cua phan tu 
print(listNumber.index(3))

# insert 1 phan tu vao 1 vi tri nao do
listNumber.insert(3, 'Ha Noi')
print(listNumber)

# Hop 2 list 
lst = listNumber2 + [1,2,3,4]
print(lst)

# Bài 1 : Chuyển một số trong phạm vi 0-99 
# thành phát âm tiếng Việt. Ví dụ : 85 → tám mươi lăm
numbers =['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu','bảy', 'tám', 'chín']

# TUPLE
tupleNumber =(1, 9, 8)
listNumber4 =list(tupleNumber)
print(listNumber4)
listNumber4.append(6)
print(listNumber4)
newtupleNumber = tuple(listNumber4)
print(newtupleNumber)