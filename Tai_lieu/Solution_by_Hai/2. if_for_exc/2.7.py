def tinh_tien_gio_bat_dau_0_den_7(gio_dung):
    if gio_dung >= 7:
        return gio_dung * 300 * 60 / 0.15
    else:
        return gio_dung * 300

def tinh_tien_gio_bat_dau_7_den_17(gio_dung):
    if gio_dung >= 6:
        return gio_dung * 400 * 60 / 0.1
    else:
        return gio_dung * 400

def tinh_tien_gio_bat_dau_17_den_24(gio_dung):
    if gio_dung >= 4:
        return gio_dung * 350 * 60 / 0.12
    else:
        return gio_dung * 350

gio_bat_dau = int(input("Nhập giờ bắt đầu: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc: "))
so_gio = gio_ket_thuc - gio_bat_dau

if gio_bat_dau >= 0 and gio_bat_dau <= 7:
    print("Số tiền cần trả là:", tinh_tien_gio_bat_dau_0_den_7(so_gio), "đồng")
elif gio_bat_dau > 7 and gio_bat_dau <= 17:
    print("Số tiền cần trả là:", tinh_tien_gio_bat_dau_7_den_17(so_gio), "đồng")
elif gio_bat_dau > 17 and gio_bat_dau <=24:
    print("Số tiền cần trả là:", tinh_tien_gio_bat_dau_17_den_24(so_gio), "đồng")
else:
    print("Giờ không hợp lệ.")
