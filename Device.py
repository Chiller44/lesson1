class Device:
    def __init__(self, power, voltage, brand, price):
        self.power = power
        self.voltage = voltage
        self.brand = brand
        self.price = price

    def device_info(self):
        print(f'Brand od device: {self.brand}, power: {self.power}, voltage {self.voltage}, price - {self.price}')

class CoffeMachine(Device):
    def __init__(self, power, voltage, brand, price, type_of_coffe, sugar):
        super().__init__(power, voltage, brand, price)
        self.type_of_coffe = type_of_coffe
        self.sugar = sugar

    def voltage1(self):
        volt = input('Введіть напругу в мережі: ')
        #volt = 220
        if volt == '380':
            print(f'Краще кавоварку бренду {self.brand} не вмикати!')
        elif volt == '220':
            print(f'Приємного використання кавоварки {self.brand}!')

    def show(self):
        print(f'{self.brand}')

panasonic = CoffeMachine('1.5 kW', '380 V', 'Panasonic', '19000 hrn', 'latte', 'without_sugar')
panasonic.voltage1()
