class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def inputInfo(self):
        self.a = float(input("Nhập độ dài cạnh a: "))
        self.b = float(input("Nhập độ dài cạnh b: "))
        self.c = float(input("Nhập độ dài cạnh c: "))

    def kiemTraTamGiac(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            if (self.a == self.b) and (self.b == self.c):
                return "Tam giác đều"
            elif (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
                return "Tam giác cân"
            else:
                return "Tam giác thường"
        else:
            return "Không phải tam giác"

    def tinhChuVi(self):
        return self.a + self.b + self.c

    def tinhDienTich(self):
        p = (self.a + self.b + self.c) / 2
        S = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return S

triangle1 = Triangle(0.0, 0.0, 0.0)
triangle1.inputInfo()
print(f"Kiểu tam giác: {triangle1.kiemTraTamGiac()}")
print(f"Chu vi tam giác: {triangle1.tinhChuVi()}")
print(f"Diện tích tam giác: {triangle1.tinhDienTich()}")
