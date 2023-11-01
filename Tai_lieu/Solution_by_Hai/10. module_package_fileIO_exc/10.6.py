filename = input("Nhập tên tập tin: ")
content = input("Nhập nội dung: ")

with open(filename, "a") as f:
    f.write(content + "\n")

while True:
    choice = input("Bạn có muốn tiếp tục ghi nội dung không? (1: có, 0: không) ")
    if choice == "1":
        content = input("Nhập nội dung: ")
        with open(filename, "a") as f:
            f.write(content + "\n")
    elif choice == "0":
        break
    else:
        print("Lựa chọn không hợp lệ!")
