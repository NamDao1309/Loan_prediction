# class Shape:
#     # attribute/ field
#     width = 0.0
#     height = 0.0

#     # constructor
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calArea(self):
#         return self.width*self.height
    
# class Retangle(Shape):
#     def __init__(self, width, height):
#         super().__init__(width, height)

# class Circle(Shape):
#     def __init__(self, width, height):
#         super().__init__(width, height)

# obj = isinstance(3, int)
# print(obj)

# b = isinstance("hello", str)
# print(b)

# c = isinstance([], (float, dict, list))
# print(c)

# d = isinstance(Shape, Shape)
# print(d)

# shape = Shape(3,4)
# e = isinstance(shape, Shape)
# print(e)




class Base1:
    def __init__(self):
        print("Xin chào")

class Base2:
    def __init__(self):
        print("Hello")

    def greeting():
        print("Ni hao")

class Sub(Base1, Base2):
    pass

obj = Sub()
Base2.greeting()