class Car:
    def __init__(self, model, year, manufacture, volume, color, price):
        self.model = model
        self.year = year
        self.manufacture = manufacture
        self.volume = volume
        self.color = color
        self. price = price

    def infoCar(self):
        print(f"Автівка {self.manufacture}, модель {self.model}, {self.color} кольору, "
              f"{self.year} року випуску, з об'ємом двигуна {self.volume} кубічних сантиментрів, вартістю {self.price} доларів")
    def convert_to_hrn(self):
        kurs = float(input('Введіть курс гривні до доллара: '))
        print(f'Вартість {self.manufacture} моделі {self.model} становить {kurs * self.price} гривень')

bmw = Car("X4", '2022', 'BMW', 2.8, 'grey', 28000)

bmw.infoCar()
bmw.convert_to_hrn()

class Book:
    def __init__(self, name, year, publish, author, price, pages):
        self.name = name
        self.year = year
        self.publish = publish
        self.author = author
        self.price = price
        self.pages = pages

    def my_book(self):
        print(f'Почав читати {self.name} видавництва {self.publish}')
        p1 = int(input(f'З якої сторінки почав читати: '))
        p2 = int(input(f'На якій сторінці закінцив читати: '))
        print(f'Залишилось прочитати до кінця книги {self.name} {self.pages - (p2 - p1)} сторінок.')

book1 = Book('Хірург', 2005, 'Веселка', 'Герітссен Тесс', '17,8$', 129)
book2 = Book('Код да Вінчі', 2004, 'Ранок', 'Ден Браун', '22,4$', 199)

book1.my_book()
book2.my_book()

class Stadium:
    def __init__(self, name, opendate, country, city, capacity):
        self.name = name
        self.opendate = opendate
        self.country = country
        self.city = city
        self.capacity = capacity


    def stadInfo(self):
        try:
            team = input("Barca or Real M??  ")
            if team != 'Barca' and team != 'Real M':
                raise Exception
            if team == 'Barca':
                print(f'{team} грає в місті {self.city} на стадіоні {self.name}, в місті {self.city},'
                      f'який вміщує {self.capacity} глядачів.')
            if team == 'Real M':
                print(f'{team} грає в місті {self.city} на стадіоні {self.name}, в місті {self.city},'
                      f'який вміщує {self.capacity} глядачів.')
        except:
            print(f'Хочу Barca чи Real M')

real_M = Stadium('Estadio Santiago Bernabéu', '14 грудня 1947 р.', 'Spain', 'Madrid', 81044)
barca = Stadium('Camp Nou', '24 ересня 1957 р.', 'Spain', 'Barcelona', 99354)

real_M.stadInfo()
barca.stadInfo()



    