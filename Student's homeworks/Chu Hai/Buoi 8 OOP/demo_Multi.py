class Vehicle:
            
        def __int__(self,_hang, _nam, _mau, _chaybang):
                self.hang= _hang
                self.nam= _nam
                self.mau= _mau
                self.chaybang= _chaybang
        def running(self):
                print("xe đang chay..")

class Xedap(Vehicle):
        hai_banh = ""

        def __int__(self,_hang, _nam, _mau, _chaybang, _hai_banh):
            super().__init__(_hang, _nam, _mau, _chaybang)
            self.hai_banh= _hai_banh
        def running(self):
                print("Xe dap", self.hang, "có màu", self.mau,"chạy bằng", self.chaybang )

class Car(Vehicle):
        bon_banh =""
        #khởi tạo
        def __int__(self,_hang, _nam, _mau, _chaybang, _bon_banh):
            super().__init__(_hang, _nam, _mau, _chaybang)
            self.bon_banh=_bon_banh
        def running(self):
                print("ô tô", self.hang, "có màu", self.mau,"chạy bằng", self.chaybang )
# khởi tạo đối tượng
Dap = Xedap("Phương hoàng",1988,"màu xanh","chạy cơ","2 bánh")
Dap.running()
Toy =Car("toy", 1989, "Trắng"," xăng","4 bánh")
Toy.running()