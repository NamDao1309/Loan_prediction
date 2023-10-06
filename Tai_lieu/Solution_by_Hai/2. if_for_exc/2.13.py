n = int(input("Nhập một số nguyên dương: "))
tong = 0
i = 1

while i <= n:
    tong += i
    i += 1

print(f"Tổng các số từ 1 đến {n} là {tong}.")
