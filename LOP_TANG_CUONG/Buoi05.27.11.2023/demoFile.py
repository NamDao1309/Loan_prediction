

path_file = "Buoi05.27.11.2023\ThuDieu.txt"
file = open(path_file, mode='rt', encoding='utf-8')
# file.writelines(
#     ['Ao thu lạnh lẽo nước trong veo \n',
#      'Một chiếc tuyền câu bé tẻo teo \n',
#      'Sóng biếc theo làn hơi gợn tí \n'
#      ]
# )

for line in file:
    print(line)
file.close()