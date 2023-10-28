s = input("Nhập chuỗi: ")
count = 0

i = 0
while i < len(s):
    if ord("0") <= ord(s[i]) <= ord("9"):
        count += 1
    i += 1

print("Số lượng ký tự là số trong chuỗi là {count}.")
