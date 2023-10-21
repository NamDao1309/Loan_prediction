# Module 2: Giải phương trình bậc hai

import math

def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return f"Nghiệm kép của phương trình là x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Nghiệm của phương trình là x1 = {x1} và x2 = {x2}"