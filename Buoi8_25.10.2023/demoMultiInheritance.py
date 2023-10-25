class Vehicle:
    # Hàm khởi tạo đối tượng
    def __init__(self,_brand, _year, _color, _engine):
        self.brand = _brand
        self.year = _year
        self.color = _color
        self.engine = _engine

    def running(self):
        print("Xe đang chạy...")

class Bicycle(Vehicle):
    hai_banh = ""
    
    # Hàm constructor của bicycle
    def __init__(self, _brand, _year, _color, _engine, _hai_banh):
        super().__init__(_brand, _year, _color, _engine)
        self.hai_banh = _hai_banh

    def running(self):
        print("Xe đạp ", self.brand, " có màu ", self.color,  "đang chạy ...")


class Car(Vehicle):
    bon_banh = ""

    # Hàm khởi tạo 
    def __init__(self, _brand, _year, _color, _engine, bon_banh):
        super().__init__(_brand, _year, _color, _engine)
        self.bon_banh = bon_banh

    def running(self):
        print("Ô tô ", self.brand, " có màu ", self.color," đang chạy ...")

# Khởi tạo đối tượng
xedap = Bicycle("Phượng Hoàng", 1990, "màu đỏ", "chạy cơ", " 2 bánh")
xedap.running()

toyota = Car("Toyota", 2001, "Màu Trắng"," chạy xăng" ," 4 bánh")
toyota.running()

# ÔN TẬP
# 1. Các kiểu dữ liệu nguyên thủy : string, float, int, array ...
# 2. Kiểu dữ liệu tập hợp : list, tuple, dict, object
# 3. Câu điều kiện : if elif, else
# 4. Vòng lặp : for, while
# 5. Hàm xử lý string, hàm xử lý số ( floor, ceil,...), 
# hàm range, hàm lambda
# 6. Lập trình OOP : kế thừa, đa hình,...
# 7. Phạm vi biến global, local
# 8. làm việc với tệp : open, write, read, append file txt
# 9. Xử lý ngoại lệ : try except finally