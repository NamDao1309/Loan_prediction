# 5.7
from modules.liet_ke_uoc_ngto import liet_ke_uoc_so_nguyen_to
from modules.tinh_tong_cs import tinh_tong_chu_so
from modules.ptich_thua_so_nto import phan_tich_thua_so_nguyen_to
from modules.liet_ke_uoc import liet_ke_uoc_so

n = int(input("Nhập số nguyên dương n: "))

print("1. Tính tổng các chữ số của n")
print("2. Phân tích n thành tích các thừa số nguyên tố")
print("3. Liệt kê các ước số của n")
print("4. Liệt kê các ước số là nguyên tố của n")

choice = input("Nhập lựa chọn của bạn (1, 2, 3, 4): ")

if choice == "1":
    tong_chu_so = tinh_tong_chu_so(n)
    print(f"Tổng các chữ số của {n} là {tong_chu_so}")
elif choice == "2":
    thua_so_nguyen_to = phan_tich_thua_so_nguyen_to(n)
    print(
        f"Phân tích {n} thành tích các thừa số nguyên tố: {thua_so_nguyen_to}")
elif choice == "3":
    uoc_so = liet_ke_uoc_so(n)
    print(f"Các ước số của {n}: {uoc_so}")
elif choice == "4":
    uoc_so_nguyen_to = liet_ke_uoc_so_nguyen_to(n)
    print(f"Các ước số là nguyên tố của {n}: {uoc_so_nguyen_to}")
else:
    print("Lựa chọn không hợp lệ")
