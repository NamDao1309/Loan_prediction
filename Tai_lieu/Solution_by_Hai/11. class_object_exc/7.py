import math

class So:
    def __init__(self, number=0):
        self.number = number

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number

    def inputNumber(self):
        self.number = int(input("Nhập số: "))

    def showNumber(self):
        print("Số hiện tại:", self.number)

    def kiemTraNguyen(self):
        return isinstance(self.number, int)

    def kiemTraChanLe(self):
        return self.number % 2 == 0

    def kiemTraAmDuong(self):
        if self.number > 0:
            return "Số dương"
        elif self.number < 0:
            return "Số âm"
        else:
            return "Zero"

    def kiemTraChanDuong(self):
        return self.number > 0 and self.number % 2 == 0

    def kiemTraLeAm(self):
        return self.number < 0 and self.number % 2 != 0

    def kiemTraChinhPhuong(self):
        return self.number >= 0 and math.isqrt(self.number) ** 2 == self.number

    def kiemTraNguyenTo(self):
        if self.number < 2:
            return False
        for i in range(2, int(math.sqrt(self.number)) + 1):
            if self.number % i == 0:
                return False
        return True

    def kiemTraHoanHao(self):
        if self.number < 1:
            return False
        total = 1
        for i in range(2, int(math.sqrt(self.number)) + 1):
            if self.number % i == 0:
                total += i
                if i != self.number // i:
                    total += self.number // i
        return total == self.number

    def kiemTraDacBiet(self):
        # Số đặc biệt nếu là số chính phương, số nguyên tố hoặc số hoàn hảo
        return self.kiemTraChinhPhuong() or self.kiemTraNguyenTo() or self.kiemTraHoanHao()

# Sử dụng lớp So
so1 = So()
so1.inputNumber()
so1.showNumber()

print("Là số nguyên:", so1.kiemTraNguyen())
print("Chẵn hay lẻ:", "Chẵn" if so1.kiemTraChanLe() else "Lẻ")
print("Dương hay âm:", so1.kiemTraAmDuong())
print("Chẵn dương:", so1.kiemTraChanDuong())
print("Lẻ âm:", so1.kiemTraLeAm())
print("Chính phương:", so1.kiemTraChinhPhuong())
print("Nguyên tố:", so1.kiemTraNguyenTo())
print("Hoàn hảo:", so1.kiemTraHoanHao())
print("Đặc biệt:", so1.kiemTraDacBiet())
