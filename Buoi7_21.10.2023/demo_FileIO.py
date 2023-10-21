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

# Bai tap 01 : Đếm số dòng của file mbox-short.txt
# Bài tập 02 : Đếm tổng tất cả các ký tự trong file 
