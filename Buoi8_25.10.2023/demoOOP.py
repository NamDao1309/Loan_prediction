
class Person:
    pass

class Student(Person):
    # Các thuộc tính - attribute
    name = ""
    age = 0
    address = ""
    id = ""
    sex = ""
    dtb = 0.0

    # hàm khởi tạo - hàm constructor
    def __init__(self, _name, _age, _address, _id, _sex, _dtb):
        self.name = _name
        self.age = _age
        self.address = _address
        self.id = _id
        self.sex = _sex
        self.dtb =_dtb

    # các phương thức ( behavior, method)
    def learning(self):
        print("Sinh Viên có tên ", self.name ,  " ở địa chỉ " , self.address, " đang học")

    def calDiemTB(self):
        print(" Sinh viên có ID = ", self.id, " có ĐTB là", self.dtb)


# Khởi tạo đối tượng
thiStudent = Student("Nguyễn Văn A", 25, "Hà Nội", "CQ101", "nam", 7.5)

# Gọi phương thức của đối tượng
thiStudent.learning()
thiStudent.calDiemTB()

# kiểm tra có phải là đối tượng ko
print(isinstance(thiStudent, Student))
print(isinstance(thiStudent, Person))
print(isinstance(3.4, float))
print(isinstance(3, str))


