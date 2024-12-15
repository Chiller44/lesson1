import random
brands_of_car = {
    'BMW': {'fuel':100, 'strength':100, 'consumption':6},
    'Volvo': {'fuel':75, 'strength':60, 'consumption':8},
    'ЗАЗ': {'fuel':45, 'strength':100, 'consumption':6},
    'Ford': {'fuel':80, 'strength':130, 'consumption':4}
}

jop_listr = {
    'Java dev': {'salary':50, 'gladness_less':10,},
    'Python dev': {'salary':40, 'gladness_less':3},
    'Assembler dev': {'salary':1000, 'gladness_less':25},
    'Swift dev': {'salary':80, 'gladness_less':2}
}
class Human:
    def __init(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)


    def eat(self):
        if self.home.food <=0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food = 5

    def work(self):
        if self.car.fuel < 20:
            self.shopping('fuel')
            return
        else:
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4

    def shopping(self, manage):



    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def day_index(self, day):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brands_of_car[self.brand]['fuel']
        self.strenght = brands_of_car[self.brand]['strength']
        self.consumpion = brands_of_car[self.brand]['consumtion']

    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumpion:
            self.fuel -= self.consumpion
            self.strenght -= 1
            return True
        else:
            print('Car cant move')
            return False
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']



