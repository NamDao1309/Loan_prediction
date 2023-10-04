# Nhập 4 số từ bàn phím
so1 = float(input("Nhập số thứ nhất: "))
so2 = float(input("Nhập số thứ hai: "))
so3 = float(input("Nhập số thứ ba: "))
so4 = float(input("Nhập số thứ tư: "))

# Tìm số lớn nhất sử dụng hàm max()
# max_so = max(so1, so2, so3, so4)

# Tìm số lớn nhất sử dụng if
if so1 > so2:
    if so1 > so3:
        if so1 > so4:
            max_so = so1
        else:
            max_so = so4
    else:
        if so3 > so4:
            max_so = so3
        else:
            max_so = so4
else:
    if so2 > so3:
        if so2 > so4:
            max_so = so2
        else:
            max_so = so4
    else:
        if so3 > so4:
            max_so = so3
        else:
            max_so = so4

# In ra số lớn nhất
print("Số lớn nhất là:", max_so)
