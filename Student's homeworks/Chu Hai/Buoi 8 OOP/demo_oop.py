class Student:
    name = ""
    age = 0
    diachi = ""
    id =""
    sex =""
    dtb = 0.0 
# các phuwong thức(bihaviorr, method)
    def __init__(self,_name, _age, _diachi,_id, _sex, _dtb):
        self.name= _name
        self.age= _age
        self.diachi= _diachi
        self.id= _id
        self.sex= _sex
        self.dtb= _dtb

        

    def hoc(self):
        print("sinh vien co ten", self.name, "dia chi", self.diachi, "đang học")

    def callDiemtb(self):
        print("sinh vien co ID =",self.id, "co dtb la", self.dtb)
pass
# khởi tạo đối tượng
thisstudent = Student("Ng van A", "22","Hà Nội", " CQ10", "Nam", 7.0)

#gọi phương thức đối tượng
thisstudent.hoc()
thisstudent.callDiemtb()
class Percen:

 pass
 # kiem tra có phải là đối tượng ko 
print( isinstance(thisstudent, Student))
print( isinstance(thisstudent, Percen))
