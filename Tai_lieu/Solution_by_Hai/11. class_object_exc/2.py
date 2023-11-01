class NhanVien:
    def __init__(self, name, age, address, salary, totalHours):
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
        self.totalHours = totalHours
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age
    def getAddress(self):
        return self.address
    def setAddress(self, address):
        self.address = address
    def getSalary(self):
        return self.salary
    def setSalary(self, salary):
        self.salary = salary
    def getTotalHours(self):
        return self.totalHours
    def setTotalHours(self, totalHours):
        self.totalHours = totalHours

    def inputInfo(self):
        self.name = input("Nhập tên nhân viên: ")
        self.age = input("Nhập tuổi nhân viên: ")
        self.address = input("Nhập địa chỉ nhân viên: ")
        self.salary = float(input("Nhập lương nhân viên: "))
        self.totalHours = int(input("Nhập tổng số giờ làm của nhân viên: "))

    def printInfo(self):
        print(f"Tên nhân viên: {self.name}")
        print(f"Tuổi nhân viên: {self.age}")
        print(f"Địa chỉ nhân viên: {self.address}")
        print(f"Lương nhân viên: {self.salary}")
        print(f"Tổng số giờ làm của nhân viên: {self.totalHours}")

    def tinhThuong(self):
        if self.totalHours >= 200:
            bonus = self.salary * 0.2
            return bonus
        elif 100 <= self.totalHours < 200:
            bonus = self.salary * 0.1
            return bonus
        else:
            return 0

nhanvien1 = NhanVien("", "", "", 0, 0)
nhanvien1.inputInfo()
nhanvien1.printInfo()
print(f"Số tiền thưởng của nhân viên là: {nhanvien1.tinhThuong()}")
