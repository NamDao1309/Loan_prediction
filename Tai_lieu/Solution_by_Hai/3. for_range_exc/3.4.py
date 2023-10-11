n = int(input("Nhập số cần kiểm tra: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    i = 2
    while i <= n // 2:
        if n % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
