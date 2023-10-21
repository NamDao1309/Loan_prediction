import math
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Liệt kê các ước số nguyên tố của n
def liet_ke_uoc_so_nguyen_to(n):
    uoc_so_nguyen_to = []
    for i in range(1, n + 1):
        if n % i == 0 and la_so_nguyen_to(i):
            uoc_so_nguyen_to.append(i)
    return uoc_so_nguyen_to