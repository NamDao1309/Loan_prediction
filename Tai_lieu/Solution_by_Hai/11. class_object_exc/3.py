class Student:
    def __init__(self, maSV, diemTB, age, classSV):
        self.maSV = maSV
        self.diemTB = diemTB
        self.age = age
        self.classSV = classSV

    def inputInfo(self):
        self.maSV = input("Nhập mã sinh viên: ")
        self.diemTB = float(input("Nhập điểm trung bình: "))
        self.age = int(input("Nhập tuổi sinh viên: "))
        self.classSV = input("Nhập lớp sinh viên: ")

    def showInfo(self):
        print(f"Mã sinh viên: {self.maSV}")
        print(f"Điểm trung bình: {self.diemTB}")
        print(f"Tuổi sinh viên: {self.age}")
        print(f"Lớp sinh viên: {self.classSV}")

    def hocBong(self):
        if self.diemTB >= 8.0:
            return True
        else:
            return False

    # Getter methods
    def getMaSV(self):
        return self.maSV

    def getDiemTB(self):
        return self.diemTB

    def getAge(self):
        return self.age

    def getClassSV(self):
        return self.classSV

    # Setter methods
    def setMaSV(self, maSV):
        self.maSV = maSV

    def setDiemTB(self, diemTB):
        self.diemTB = diemTB

    def setAge(self, age):
        self.age = age

    def setClassSV(self, classSV):
        self.classSV = classSV

student1 = Student("", 0.0, 0, "")
student1.inputInfo()
student1.showInfo()
if student1.hocBong():
    print("Sinh viên này được học bổng")
else:
    print("Sinh viên này không được học bổng")
