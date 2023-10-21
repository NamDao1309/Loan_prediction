# Module 3: Tính chu vi và diện tích các hình

import math
# Hình tròn
def tinh_chu_vi_hinh_tron(r):
    chu_vi = 2 * math.pi * r
    return chu_vi

def tinh_dien_tich_hinh_tron(r):
    dien_tich = math.pi * r**2
    return dien_tich

# Hình chữ nhật
def tinh_chu_vi_hinh_chu_nhat(a, b):
    chu_vi = 2 * (a + b)
    return chu_vi

def tinh_dien_tich_hinh_chu_nhat(a, b):
    dien_tich = a * b
    return dien_tich

# Hình tam giác
def tinh_chu_vi_hinh_tam_giac(a, b, c):
    chu_vi = a + b + c
    return chu_vi

def tinh_dien_tich_hinh_tam_giac(a, b, c):
    p = (a + b + c) / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return dien_tich

