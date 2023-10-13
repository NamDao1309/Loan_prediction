#bai 4_1
# n = int(input("Nhập n: "))
# a = []
# for i in range(n):
#     listSo = int(input())
#     listSo2 = listSo * listSo
#     a.append(listSo2)
# print(a)

#bai 4_2
# list1 = ["M", "na",  "i",  "Pe"]
# list2 = ["y", "me", "s", "ter"]

# listKetHop = []
# for i in range(len(list1)):
#     listKetHop.append(list1[i] + list2[i])
# print(listKetHop)

#bai 4_3
# list1 = ["Hello", "Take"]
# list2 = ["Dear",  "Sir"]

# listKetHop = []
# for i in list1:
#     for j in list2:
#         listKetHop.append(i + " " + j)
# print(listKetHop)

#bai 4_4
# n = int(input("Nhập số phần tử của chuỗi: "))
# a = []
# for item in range(n):
#     item = int(input())
#     if(item != 20):
#         a.append(item)
   
# print(a)

#bai 4_6

# so_chu = {
#     '0': 'không',
#     '1': 'một',
#     '2': 'hai',
#     '3': 'ba',
#     '4': 'bốn',
#     '5': 'năm',
#     '6': 'sáu',
#     '7': 'bảy',
#     '8': 'tám',
#     '9': 'chín'
# }

# n = input("Nhập n: ")

# danh_sach_chu = [so_chu[ch] for ch in n]

# print(" ".join(danh_sach_chu))

#bai 4_7
# gadget = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00, "Television", 1000, "Laptop Case", "Camera Lens"]

# listSo = []
# listChuoi = []

# for item in gadget:
#     if isinstance(item, (int, float)):
#         listSo.append(item)
#     elif isinstance(item, str):
#         listChuoi.append(item)

# listSo.sort()
# listChuoi.sort()
# print(listSo)
# print(listChuoi)

# listSo.sort(reverse=True)
# print(listSo)
# listChuoi.sort(reverse=True)
# print(listChuoi)

#bai 4_8
n = int(input("Nhập số phần tử: "))
a = []
max = int()
max2 = int()
for item in range(n):
    item = int(input())
    a.append(item)

    if item > max:
        max2 = max
        max = item
    elif item > max2 and item != max:
        max2 = item
    
print("Hai phần tử lớn nhất là: ", max, " ", max2)



