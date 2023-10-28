# 3.6
n = int(input('Nhap n: '))

a = []
sum = 0
for i in range(n):
    a.append(int(input('Nhap phan tu thu %d: ' % (i + 1))))
    sum += a[i]
print(sum)