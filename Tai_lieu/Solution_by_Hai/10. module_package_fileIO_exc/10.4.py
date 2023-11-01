import math

def calculate_A(x, y):
    if 2*x + 7*y == 0:
        raise ValueError("Error: division must be <> 0")
    else:
        A = (5*x - y) / (2*x + 7*y)
        if A < 0:
            raise ValueError("Error : square root must be >= 0")
        else:
            A = math.sqrt(A)
            return A

try:
    x = float(input("Nhập x: "))
    y = float(input("Nhập y: "))
    print(f"Kết quả của biểu thức A = sqrt((5x - y) / (2x + 7y)) là {calculate_A(x, y)}")
except ValueError as e:
    print(e)
