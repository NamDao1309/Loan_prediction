n = int(input("Nhập số hàng của tam giác: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
