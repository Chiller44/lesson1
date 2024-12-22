class Car:
    def __init__(self, year):
        self.__year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if 1900 < year < 2300:
            self.__year = year
        else:
            print('Error year')

bmw = Car(2000)
bmw.year = 3000
print(bmw.year)





