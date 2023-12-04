# abstract class
class Polygon:
    # abstract method
    def display(self):
        pass


class Triangle(Polygon):
    # override abstract method
    def display(self):
        print("I have 3 sides")

class Pentagon(Polygon):
    # override abstract method
    def display(self):
        print("I have 5 sides")

class Hexagon(Polygon):
    # override abstract method
    def display(self):
        print("I have 6 sides")

class Quad(Polygon):
    # override abstract method
    def display(self):
        print("I have 4 sides")

tam_giac = Quad()
tam_giac.display()

luc_giac = Hexagon()
luc_giac.display()