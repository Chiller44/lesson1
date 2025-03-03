import abc

class Shape(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abc.abstractmethod
    def area(self):
        pass

    def print_point(self):
        print(f'X: {self.x}\tY: {self.y}')

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x,y)
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

rect = Rectangle(10, 20, 100 ,20)
rect.print_point()
print(rect.area())

circ = Circle(20, 40, 10)
print(circ.area())