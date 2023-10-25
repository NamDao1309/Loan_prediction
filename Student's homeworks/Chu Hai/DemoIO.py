############################## Đọc file
file_path = "VIETECH_DA_28.09.2023//Student's homeworks//Chu Hai//tho.txt"
# file = open(file_path, mode ='rt', encoding='utf-8')
# strs = file.read()
# print(strs)

# file.close()
######################################
#viet file
file = open(file_path,mode='at', encoding=('utf-8'))
file.writelines(
   [ '\n',
    'xin chao\n',
    'Toi là hải'
   ]
)
file.close()
#######################################

