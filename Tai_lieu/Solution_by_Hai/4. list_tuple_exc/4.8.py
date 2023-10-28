# 4.8
list = []
while (True):
    try:
        numb = int(input("Nhập số: "))
    except ValueError:
        break
    list.append(numb)

list.sort()
print(list)
print(list[-2], list[-1])