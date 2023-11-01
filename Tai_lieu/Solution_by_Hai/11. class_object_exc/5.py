class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def inputInfo(self):
        self.length = float(input("Nhập chiều dài hình chữ nhật: "))
        self.width = float(input("Nhập chiều rộng hình chữ nhật: "))

    def tinhDienTich(self):
        return self.length * self.width

    def tinhChuVi(self):
        return 2 * (self.length + self.width)

rectangle1 = Rectangle(0.0, 0.0)
rectangle1.inputInfo()
print(f"Diện tích hình chữ nhật: {rectangle1.tinhDienTich()}")
print(f"Chu vi hình chữ nhật: {rectangle1.tinhChuVi()}")
