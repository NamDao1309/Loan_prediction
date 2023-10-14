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


# Dictionary
dictFruit ={
    1: 'Apple',
    2 : 'Banana',
    3 : 'Mango',
    4 : 'Kiwi'
}

print(dictFruit[1])
print(dictFruit[2])
print(dictFruit)

dict = {
    'brand' : 'Toyota',
    'year' : 2018,
    'color' : 'red',
    'price' : 50000
}

print(dict['brand'])

dict['brand'] = 'Ford'

print(dict)
print(len(dict))
print(type(dict))

# Truy cap phan tu dict
print(dict['color'])

# Get value of model
print(dict.get('color'))

# list all keys
print(dict.keys())

# list all values
print(dict.values())

# update dictionary
dict.update({'color':'blue'})
print(dict)

# add item into dict
dict['power'] = 500
dict['country'] = ['VietNam', 'Japan', 'China']
print(dict)

# remove item
dict.pop('country')
print(dict)

del dict['power']
print(dict)

# del dict
# print(dict)

# make clear dict
# dict.clear()
# print(dict)

# Duyet cac phan tu cua dict
for x in dict:
    #print(x)  #==> hien thi key
    print(dict[x])

for y in dict.keys():
    print(y)

for z in dict.values():
    print(z)

for x,y in dict.items():
    print(x,y)

# copy dict
dict2 = {}
dict2 = dict.copy()

print(dict2)

# Bai tap  : Đếm tần suất hiện của các từ trong một câu
text = 'Một năm có mười hai tháng, tháng hai có hai mươi tám ngày, các tháng còn lại có ba mươi hoặc ba mươi mốt ngày'

text = text.lower()
text = text.replace(',','')

dict_word = {}

list_word = text.split()
print(list_word)

for word in list_word:
    dict_word[word] = dict_word.get(word, 0) + 1

print(dict_word)

# bai 2 :
#Giá nước sinh hoạt tại Hà Nội được tính theo các 
# mức giá sau:
#
#Từ 0-10 m3 : 5973 đ/m3
#Từ 10-20 m3 : 7052 đ/m3
#Từ 20-30 m3 : 8669 đ/m3
#Trên 30 m3 : 15929 đ/m3
# Viết chương trình để in ra hóa đơn tiền nước 
# của một hộ gia đình. Đầu vào là khối lượng 
# nước tiêu thụ (tính theo m3) trong tháng, 
# đầu ra là chi tiết các mức phí tương ứng với các mức giá, 
# và tổng số tiền.

m3 = float(input('Khối lượng nước tiêu thụ :'))

price_table =[
    {'price' : 5973, 'muc_tieu_thu': 10},
    {'price' : 7052, 'muc_tieu_thu': 20},
    {'price' : 8669, 'muc_tieu_thu': 30},
    {'price' : 15929}
]

total = 0
#  0<m3<= 10
if(m3>= 0 and m3 <=price_table[0]['muc_tieu_thu']):
    total =  m3*price_table[0]['price'] 
# 10<m3<=20
elif(m3>price_table[0]['muc_tieu_thu'] and m3<=price_table[1]['muc_tieu_thu']):
    total = 10 * price_table[0]['price'] + (m3 -10) * price_table[1]['price']
# 20<m3<=30   
elif(m3>price_table[1]['muc_tieu_thu'] and m3<=price_table[2]['muc_tieu_thu']):
    total =  10 * price_table[0]['price'] + 10 * price_table[1]['price'] + (m3 - 20)* price_table[2]['price']
# m3>30   
else:
    total = 10 * price_table[0]['price'] + 10 * price_table[1]['price'] + 10* price_table[2]['price'] + (m3-30)*price_table[3]['price']

print("Tổng tiền :",total)

# Bai 3 :
# Tinh ra hóa đơn tiền điện của một hộ gia đình. 
# Các mức giá tiền điện như sau:


# Từ 0 - 50 KWh : 1.549 đ/KWh
# Từ 51 - 100 KWh : 1.600 đ/KWh
# Từ 101 - 200 KWh : 1.858 đ/KWh
# Từ 201 - 300 KWh : 2.340 đ/KWh
# Từ 301 - 400 KWh : 2.615 đ/KWh
# Từ 401 KWh  trở lên : 2.701 đ/KWh