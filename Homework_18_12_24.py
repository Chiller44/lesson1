import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 2
        self.alive = True

    def to_study(self):
        print("I'm study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I'm sllep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.progress -= 0.1
        self.gladness += 5
        self.money -= 25

    def to_work(self):
        print('Im goinng to work')
        self.progress += 0.5
        self.gladness -= 7
        self.money += 50

    def is_alive(self):
        if self.progress < -0.5:
            print("Відрахували")
            self.alive = False
        elif self.gladness <= 0:
            print("Йому потрібний друг")
            self.alive = False
        elif self.progress > 5:
            print("Закінчив курс екстерном")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")
        print(f'Money - {self.money}')

    def live(self, day):
        print(f"Day {day} of {self.name}")

        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()

        self.end_of_day()
        self.is_alive()

bohdan = Student("Bohdan")
for day in range(355):
    if bohdan.alive == False:
       break
    bohdan.live(day)

"""РОзширте клас студента, додавши йому арибуи гроші, реалізуйте можливість заробітку,
    під час відпочинку гроші витрачаються.
   Глибще продумайте поведінку студента, наприклад, якщо пракує коштів, він має піти на роботу, якщо проблеми з навчанням то вчиться"""