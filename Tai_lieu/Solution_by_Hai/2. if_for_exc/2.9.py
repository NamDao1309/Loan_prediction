so = int(input("Nhập số cần tính tổng các chữ số: "))
tong = 0

while so > 0:
    tong += so % 10
    so //= 10

print(f"Tổng các chữ số trong số {so} là {tong}.")
