class SoHoc:
    def __init__(self):
        self.number1 = 0
        self.number2 = 0

    def get_number1(self):
        return self.number1

    def set_number1(self, number1):
        self.number1 = number1

    def get_number2(self):
        return self.number2

    def set_number2(self, number2):
        self.number2 = number2

    def inputInfo(self):
        self.number1 = int(input("Nhập số thứ nhất: "))
        self.number2 = int(input("Nhập số thứ hai: "))

    def printInfo(self):
        print("Số thứ nhất là:", self.number1)
        print("Số thứ hai là:", self.number2)

    def addition(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multi(self):
        return self.number1 * self.number2

    def division(self):
        if self.number2 == 0:
            return "Không thể chia cho 0"
        else:
            return self.number1 / self.number2
