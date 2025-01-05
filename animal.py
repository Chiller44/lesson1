class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f'Dog {self.name} is barking')

class Cat(Animal):

    def meow(self):
        print(f'{self.name} says meow')


class Frog(Animal):

    def eat(self):
        print(f'Frog {self.name} is eating')

dog = Dog("Jack", 'colli')
cat = Cat('Tom')
frog = Frog('Green')

dog.bark()
dog.eat()
dog.breed
cat.meow()
frog.eat()


