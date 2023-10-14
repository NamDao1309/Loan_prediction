# 4.7
gadgets = ["Mobile", "Laptop", 100, "Camera", 310.28, "Speakers", 27.00,"Television", 1000, "Laptop Case", "Camera Lens"]

# Tạo hai list, một list chỉ chứa chuỗi và một list chỉ chứa số từ list cho ở trên.

listNum = []
listStr = []

for i in gadgets:
    if (type(i) == int or type(i) == float):
        listNum.append(i)
    else:
        listStr.append(i)
print(listNum)
print(listStr)

# Sắp xếp list chứa chuỗi theo thứ tự tăng dần
print(sorted(listStr))

# Sắp xếp list chứa chuỗi theo thứ tự giảm dần
print(sorted(listStr, reverse=True))

# Sắp xếp list chứa số theo thứ tự tăng dần
print(sorted(listNum))

# Sắp xếp list chứa số theo thứ tự giảm dần
print(sorted(listNum, reverse=True))
