# Tính tổng các chữ số của n
def tinh_tong_chu_so(n):
    tong = 0
    while n > 0:
        digit = n % 10
        tong += digit
        n //= 10
    return tong
