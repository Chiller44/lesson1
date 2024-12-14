class BankAccount:
    def __init__ (self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        self.balance +=200

    def withdraw(self):
        if self.balance - 300 < 0:
            print('jjj')
        else:
            self.balance -=300

class Car:
    def __init__(self, make,model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print(self.year, self.model, self.make)
bmw = Car('bmw', 'x5', '2024')
bmw.get_info()

class Employee:
    def __init__ (self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        print(f'Заробітна плата {self.name}: {self.salary}')

petrov = Employee('Petrov', 'driver', '5000 грн.')
petrov.get_salary_info()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        print(f'Загальна вартість {self.price * self.quantity}')

    def display_info(self):
        print(self.name)

tovar = Product('яйце', 6, 30)
tovar.calculate_total_price()
tovar.display_info()

