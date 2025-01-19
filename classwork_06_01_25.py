class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


v1 = Vector(2, 5)
v2 = Vector(3,7 )
v3 = v1 + v2
print(v3)



