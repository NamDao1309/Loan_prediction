file_path = "VIETECH_DA_28.09.2023//Buoi7_21.10.2023//romeo.txt"

# READ FILE
# file = open(file_path, mode='rt', encoding='utf-8')
# strs = file.readlines()
# print(strs)

# file.close()

# WRITE FILE
file = open(file_path, mode='at', encoding='utf-8')
file.writelines(
    ['\n',
     'Ao thu lạnh lẽo nước trong veo \n',
     'Một chiếc thuyền câu bé tẻo teo'
     ]
)
file.close()

# Bài tập 01 : Đếm số dòng của file mbox-short.txt
# Bài tập 02 : Tìm kiếm tất cả các dòng bắt đầu 
# là "From:"
# Bài tập 03 : Lọc tất cả các email có định dạng
# X#Y.Z và lưu vào 1 list, remove các email duplicate

# DEMO JSON
import json
x = '{"name" : "John","age" : 30,"city" : "New York" }'

# parse ison file
y = json.loads(x)

# print result
print(y["age"])

# Read file json
json_file_path = "VIETECH_DA_28.09.2023//Buoi7_21.10.2023//user.json"
with open(json_file_path) as user_file:
    file_content = user_file.read()

print(file_content)