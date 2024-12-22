class Animal:
    def __init__(self, male, year):
        self.male = male
        self.year = year

    def animal_info(self):
        print(f'Animal: {self.male}, {self.year}')

class Human(Animal):
    def __init__(self, male, year, wight):
        super().__init__(male, year)
        self.wight = wight


    def human_info(self):
        print(f'{self.wight}')

    def human_animal(self):
        print(f'{self.year}')


lion = Animal('predator', 2000)
andrii = Human('human', 1976,90)

lion.animal_info()
andrii.human_info()
andrii.animal_info()


