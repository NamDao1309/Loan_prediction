a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

uscln = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        uscln = i

print(f"USCLN của {a} và {b} là: {uscln}")
