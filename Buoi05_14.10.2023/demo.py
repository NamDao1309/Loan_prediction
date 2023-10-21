# Dictionary
dictFruit = {
    1 : 'Apple',
    2 : 'Banana',
    3 : 'Mango',
    4 : 'Kiwi'
}

print(dictFruit)

dict = {
    'brand' : 'Toyota',
    'year' : 2018,
    'color' : 'red',
    'price' : 50000
}

# print(dict['brand'])

# dict['brand'] = 'Ford'
# print(len(dict))
# print(type(dict))

# #Truy cập phần tử dict
# print(dict['color'])

# #get value
# print(dict.get('color'))

# #list all keys
# print(dict.keys())

# #list all values
# print(dict.values())

# #update dictionary
# dict.update({'color' : 'blue'})
# print(dict)

# #add item into dict
# dict['power' ] = 500
# dict['country'] = ['Vietnam', 'Japan', 'China']
# print(dict)

# #remove item
# dict.pop('country')
# print(dict)

# # del dict['power']
# # print(dict)

# # del dict

# #make clear dict
# dict.clear()
# print(dict)

#duyet các phần tử của dict
# for x in dict:
#     print(x)  #==> hiển thị key
#     print(dict[x])

# for y in dict.keys():
#     print(y)

# for z in dict.values():
#     print(z)

# for x, y in dict.items():
#     print(x,y)

# #copy dict
# dict2 = {}
# dict2 = dict.copy()
# print(dict2)

#bài tập

text = 'Một năm có mười hai tháng, tháng hai có hai mươi tám ngày, các tháng còn lại có ba mươi hoặc ba mốt ngày'
# result = {}
# result['Một'] = text.count('Một')
# result['năm'] = text.count('năm')
# result['có'] = text.count('có')
# result['mười'] = text.count('mười')
# result['hai'] = text.count('hai')
# result['tháng'] = text.count('tháng')
# result['mươi'] = text.count('mươi')
# result['tám'] = text.count('tám')
# result['ngày'] = text.count('ngày')
# result['các'] = text.count('các')
# result['còn'] = text.count('còn')
# result['lại'] = text.count('lại')
# result['ba'] = text.count('ba')
# result['hoặc'] = text.count('hoặc')
# print(result)

# text = text.lower()
# text = text.replace(',' , '')

# dict_word = {}
# list_word = text.split()
# print(list_word)
# for word in text.split():
#     dict_word[word] = dict_word.get(word, 0) + 1

# print(dict_word)

# bai 2:
n = int(input("Nhập vào số m3 nước: "))
tien_nuoc = {}
if (n > 0 and n <= 10):
    tien_nuoc['Hóa đơn tiền nước: '] = n * 5973
elif (n > 10 and n <= 20):
    tien_nuoc['Hóa đơn tiền nước: '] = (10 * 5973) + (n - 10) * 7052
elif (n > 20 and n <= 30):
    tien_nuoc['Hóa đơn tiền nước: '] = (10 * 5973) + (10 * 7052) + (n - 20) * 8669
else:
    tien_nuoc['Hóa đơn tiền nước: '] = (10 * 5973) + (10 * 7052) + (10 * 8669) + (n - 30) * 15929

print(tien_nuoc)

#bai 3:






