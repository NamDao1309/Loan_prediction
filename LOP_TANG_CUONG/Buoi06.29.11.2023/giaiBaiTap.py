# Bài 4.5*:
# Tìm tất cả các từ duy nhất trong một tệp
# Viết chương trình để mở tệp romeo.txt và đọc từng dòng một. Đối với mỗi dòng, chia
# dòng thành danh sách các từ bằng cách sử dụng chức năng tách. Đối với mỗi từ, hãy kiểm
# tra xem từ đó đã có trong danh sách các từ duy nhất chưa. Nếu từ không có trong danh
# sách các từ duy nhất, hãy thêm từ đó vào danh sách.

file_path = "Buoi06.29.11.2023//romeo.txt"
wordlist = list()
file = open(file_path, mode='rt', encoding='utf-8')
for line in file:
    words = line.split(" ")
    for word in words:
        if word in wordlist: continue
        wordlist.append(word)

wordlist.sort()
print(wordlist)