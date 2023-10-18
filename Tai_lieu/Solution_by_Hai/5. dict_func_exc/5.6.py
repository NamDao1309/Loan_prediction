# 5.6
import math
from modules.pt_bac_1 import giai_phuong_trinh_bac_nhat
from modules.pt_bac_2 import giai_phuong_trinh_bac_hai
from modules.tinh_cv_dt import *
# Chương trình chính

print("1. Giải phương trình bậc nhất")
print("2. Giải phương trình bậc hai")
print("3. Tính chu vi và diện tích các hình")
choice = input("Nhập lựa chọn của bạn (1, 2, 3): ")

if choice == "1":
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    result = giai_phuong_trinh_bac_nhat(a, b)
    print(result)
elif choice == "2":
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    result = giai_phuong_trinh_bac_hai(a, b, c)
    print(result)
elif choice == "3":
    print("1. Hình tròn")
    print("2. Hình chữ nhật")
    print("3. Hình tam giác")
    shape_choice = input("Nhập lựa chọn của bạn (1, 2, 3): ")
    
    if shape_choice == "1":
        r = float(input("Nhập bán kính hình tròn: "))
        chu_vi = tinh_chu_vi_hinh_tron(r)
        dien_tich = tinh_dien_tich_hinh_tron(r)
        print(f"Chu vi hình tròn là {chu_vi}")
        print(f"Diện tích hình tròn là {dien_tich}")
    elif shape_choice == "2":
        a = float(input("Nhập chiều dài hình chữ nhật: "))
        b = float(input("Nhập chiều rộng hình chữ nhật: "))
        chu_vi = tinh_chu_vi_hinh_chu_nhat(a, b)
        dien_tich = tinh_dien_tich_hinh_chu_nhat(a, b)
        print(f"Chu vi hình chữ nhật là {chu_vi}")
        print(f"Diện tích hình chữ nhật là {dien_tich}")
    elif shape_choice == "3":
        a = float(input("Nhập cạnh a của tam giác: "))
        b = float(input("Nhập cạnh b của tam giác: "))
        c = float(input("Nhập cạnh c của tam giác: "))
        chu_vi = tinh_chu_vi_hinh_tam_giac(a, b, c)
        dien_tich = tinh_dien_tich_hinh_tam_giac(a, b, c)
        print(f"Chu vi hình tam giác là {chu_vi}")
        print(f"Diện tích hình tam giác là {dien_tich}")
else:
    print("Lựa chọn không hợp lệ")