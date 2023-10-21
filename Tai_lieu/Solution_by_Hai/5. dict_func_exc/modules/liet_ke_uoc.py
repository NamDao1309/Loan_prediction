# Liệt kê các ước số của n
def liet_ke_uoc_so(n):
    uoc_so = []
    for i in range(1, n+1):
        if n % i == 0:
            uoc_so.append(i)
    return uoc_so
