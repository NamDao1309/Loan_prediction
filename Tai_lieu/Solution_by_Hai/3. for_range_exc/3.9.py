
# 3.9
# a.
n1 = int(input('Nhap n1: '))

for i in range(1, n1 + 1):
    for j in range(1, i + 1):
        print('*', end='')
    print()

# b.
n2 = int(input('Nhap n2: '))
m2 = int(input('Nhap m2: '))

for i in range(1, n2 + 1):
    for j in range(1, m2 + 1):
        print('*', end='')
    print()

# c.
n3 = int(input('Nhap n3: '))

for i in range(1, n3 + 1):
    for j in range(1, 2 * i):
        print('*', end='')
    print()
