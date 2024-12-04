class Rectangle:
    def __init__(self,w, h):
        self.heigth = w
        self.length = h

    def area(self):
        return self.length * self.heigth

    def perim(self):
        return 2 * (self.length + self.heigth)

f = Rectangle(6, 10)

print(f.area())
print(f.perim())