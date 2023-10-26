so_tien_vay = 400_000_000
lai_suat = 0.1
tra_tien_thang = 10_000_000

tong_no = so_tien_vay * (1 + lai_suat)
so_thang = 0

while tong_no > 0:
    tong_no -= tra_tien_thang
    tong_no *= (1 + lai_suat / 12)
    so_thang += 1

print(f"Số tháng cần trả nợ là {so_thang}.")
