# txt = "Welcome to Python For Everybody"
# print("Python" in txt)
# print("Python" not in txt)
# print(txt.upper())
# print(txt.lower())
# print(txt.split(' '))
# print(txt.replace('Python', "Java"))

# #String Format
# print("Tôi được {0} điểm Toán và {1} điểm Văn".format(8.5, 7.8))

# name = "Mậu"
# age = 20
# x = 'A'
# print(f"Xin chào, Tên tôi là {name}, tôi {age} tuổi")
# print('Ký tự %c' %(x))
# print('họ và Tên : %s' %('Hoàng Hoa Thám'))
# print("Số tự nhiên : %d %i %u" %(10, 3, 5.4))
# print("Số octal : %o" %(30))

# -------------------------------
# listFruit = ['Lê', 'Thị', 'Mận', 'Đào']
# print(listFruit)

# listNumber = [3, 9, 2, 5, -10]
# print(listNumber)

# listItem = ['Apple', True, 3.5, 'B', ["Toán", "Lý", "Hóa"]]
# print(listItem)
# print(listItem[4][1])

# #Slicing
# print(listItem[1:4])
# print(listItem[:4])
# print(listItem[3:])

# #lấy độ dài
# print(len(listItem))

# #đảo ngược list item
# listItem.reverse()
# print(listItem)

# #Sắp xếp
# listNumber.sort()
# listNumber.sort(reverse=True)
# print(listNumber)

# #add number
# listNumber.append(6)
# listNumber.append(6)
# print(listNumber)

# #delete number
# listNumber.remove(6)
# print(listNumber)

# #delete item with position
# print(listNumber.pop(3))
# print(listNumber.pop())  #get item ở đầu stack

# listFloat = [4.6, 2.9, 7.0, -5.8]


# # Hợp 2 list thành 1
# listNumber.extend(listFloat)
# print(listNumber)

# xóa tất cả phần tử
# listNumber.clear()
# print(listNumber)

# hủy một list
# del listNumber
# print(listNumber)

#copy list
#cach 1
# listNumber2 = listNumber
# print(listNumber2)

#cach 2
# listNumber = listNumber.copy()
# print(listNumber3)

#đếm số phần tử xuất hiện
# print(listNumber.count(3))

#lấy chỉ số index của phần tử
# print(listNumber.index(3))

#insert một phần tử vào 1 vị trí nào đó
# listNumber.insert(3, 'Hà Nội')
# print(listNumber)

# #hợp 2 list
# lst = listNumber + [1, 2, 3, 4]
# print(lst)

#Bài 1: Chuyển một số trong phạm vi 0 - 99 thành phát âm tiếng việt 
# numbers = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín' ,'mười']

# n = int(input("Nhập một số bất kì từ 0 - 99: "))
# while n < 0 or n > 99:
#     print("Lỗi, n phải trong khoảng từ 0 đến 99")
#     break

# tuple
tupleNumber = (1, 9, 8)
listNumber4 = list(tupleNumber)
print(listNumber4)
listNumber4.append(6)
print(listNumber4)
newtupleNumber = tuple(listNumber4)
print(newtupleNumber)


