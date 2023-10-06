import math

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Diện tích:", area)
else:
    print("Đây không phải là 3 cạnh của một tam giác")
