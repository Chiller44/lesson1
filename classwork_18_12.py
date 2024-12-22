class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f'Name: {self.__name}')

class Employee(Person):
    def __inint__(self, name, company):
        super().__init__(name)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f'company: {self.company}')

    def work(self):
        print(f'{self.__name} works.')


tom = Employee('Tom')
tom.display_info()
tom.work()