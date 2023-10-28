so = int(input("Nhập số cần đảo ngược: "))
so_dao_nguoc = 0

while so > 0:
    so_dao_nguoc = so_dao_nguoc * 10 + so % 10
    so //= 10

print(f"Số đảo ngược của {so} là {so_dao_nguoc}.")
