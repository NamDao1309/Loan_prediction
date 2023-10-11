# 3.8
n = int(input('Nhap n: '))

cnt = 0
sum = 0
i = 2
while (True):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        cnt += 1
        sum += i
    if (cnt == n):
        print(sum)
        break
    i += 1