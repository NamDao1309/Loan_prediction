thang = int(input("Nhập tháng (1-12): "))

if thang in [3, 4, 5]:
    mua = "Mùa xuân"
elif thang in [6, 7, 8]:
    mua = "Mùa hè"
elif thang in [9, 10, 11]:
    mua = "Mùa thu"
else:
    mua = "Mùa đông"

print("Mùa của tháng", thang, "là", mua)
