class Human:
    def __init__(self, name = 'Human'):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_pessengers_names(self):
        if self.passengers != []:
            print(f'Name of {self.brand} passengers: ')
            for p in self.passengers:
                print(p.name)
            else:
                print(f'No passengers in {self.brand}')
nik = Human('Nick')
kate = Human('Kate')
car = Auto('Mersedes')
car.add_passenger(nik)

car.print_pessengers_names()


