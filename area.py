class Circle:
    radius = 10
    cphai = 22/7
    def every_area(self):
        return self.cphai*self.radius*self.radius

class Rectangle:
    length = 10
    breadth = 3
    def every_area(self):
        return self.length*self.breadth

class Square:
    length = 10
    def every_area(self):
        return self.length*self.length

objcir = Circle()
objrec = Rectangle()
objsqu = Square()

print(objcir.every_area())
print(objsqu.every_area())
print(objrec.every_area())
