file_name = input("Nhập tên tập tin:\n")

with open(file_name, "r") as f:
    content = f.read()
    print('Nội dung tập tin:\n', content)
