############################## Đọc file
file_path = "VIETECH_DA_28.09.2023//Student's homeworks//Chu Hai//tho.txt"
# file = open(file_path, mode ='rt', encoding='utf-8')
# strs = file.read()
# print(strs)

# file.close()
######################################
#viet file
# file = open(file_path,mode='at', encoding=('utf-8'))
# file.writelines(
#    [ '\n',
#     'xin chao\n',
#     'Toi là hải'
#    ]
# )
# file.close()
#######################################
# Bài 1 đếm số dòng của file mbox-short.txt
# Bài 2 tìm tất cả các dòng bắt đầu từ  "from"
# Bài 3 Lọc các email có định dạng x#y.z và lưu vào 1 list

#demo json
import json
x='{"name": "jonh", "age" : 30, "city" : "HN" }'

y= json.load(x)
print(y["age"])
