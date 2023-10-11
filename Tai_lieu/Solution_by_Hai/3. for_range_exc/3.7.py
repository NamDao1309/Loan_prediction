# 3.7
n = int(input('Nhap n: '))
sum = 0

for i in range(2, n):
    # check if i is prime
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        sum += i
        print(i)
print(sum)