# Phân tích số n thành tích các thừa số nguyên tố
def phan_tich_thua_so_nguyen_to(n):
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors
