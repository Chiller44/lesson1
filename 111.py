
class People:
    def __init__(self, name, birthday, phone, city, country):
        self.name = name
        self.birthday = birthday
        self.phone = phone
        self.city = city
        self.country = country



    def inPut(self):
        print(f'Hello, {self.name}')
        print(f'How are yuo, {self.name}?')

p1 = People('Bob', 2024, '+1111', 'Kiyv', 'Ukraine')
p1.inPut()








