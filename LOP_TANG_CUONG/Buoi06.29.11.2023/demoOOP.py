# class Dog:
#     # attribute/ field
#     breed = " "
#     size = " "
#     color = " "
#     age = 0

#     # contructor default
#     def __init__(self, _bread, _size, _color, _age):
#         self.breed = _bread
#         self.size = _size
#         self.color = _color
#         self.age = _age

#     # method, behavior
#     def eat(self):
#         print("Chó " + self.breed + " đang ăn" )

#     def run(self):
#         print("Chó " + self.breed + " có màu lông " + self.color + " đang chạy")

#     def sleep(self):
#         print("Chó " + self.breed + " tuổi " + str(self.age) + " đang ngủ")


# # khởi tạo đối tượng
# dogObject = Dog("Bulldog", "cỡ lớn","màu đen", 4 )

# # truy cập phương thức
# dogObject.eat()
# dogObject.run()
# dogObject.sleep()


import math

class Circle:
    # thuộc tính
    radius = 0.0

    # hàm khởi tạo
    def __init__(self, r):
        self.r = r

    # phương thức
    def calPerimeter(self):
        return 2*math.pi*self.r
    
    def calArea(self):
        return math.pi*self.r*self.r
    
# khởi tạo đối tượng
objCircle = Circle(15.4)
print("Chu vi hình tròn là : ", objCircle.calPerimeter())
print("Diện tích hình tròn là : ", objCircle.calArea())
