#bai 1
# dict1 = {
#     'car' : 'ô tô',
#     'phone' :'điện thoại',
#     'bike' : 'xe đạp',
#     'box' : 'hộp',
#     'apple' : 'quả táo',
#     'door' : 'cửa',
#     'computer' : 'máy tính',
#     'bed' : 'giường'
# }

# name = input("Name word: ")
# translation = dict1.get(name, 'Không tìm thấy từ cần dịch')
# print(f"{translation}")

#bài 2

text = 'Một năm có mười hai tháng, tháng hai có hai mươi tám ngày, các tháng còn lại có ba mươi hoặc ba mốt ngày'

text = text.lower()
text = text.replace(',' , '')

dict_word = {}
list_word = text.split()
print(list_word)
for word in text.split():
    dict_word[word] = dict_word.get(word, 0) + 1

print(dict_word)