class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self.__age = age

    def describe(self):
        print(f"I'm {self._first_name} {self._last_name}. I'm {self.__age}")

    def set_age(self, age):
        if age < 1 or age > 100:
            raise ValueError (f'Age must be range 1-100')
        self.__age = age


tom = Person('Andrii', 'Brezhnev', 48)
tom.set_age(500)
tom.describe()
