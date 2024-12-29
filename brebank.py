class Brebank:
    def __init__(self, first_name, last_name, age, tel_number, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.tel_number = tel_number
        self.pin = pin
        self.balance = balance
        self.usd = 0
        self.gbp = 0
        self.euro = 0

    def password(self):
        a = 0
        b = 4
        while True:
            passw = int(input('Введіть свій pin-код: '))
            if passw == self.pin:
                andrii.menu()
                return False
            else:
                a += 1
                b -= 1
                print(f'Невірний pin-код. Спробуйте ще раз. У Вас є ще {b - 1} спроби. Потім карта буде заблокована!')
                if a == 3:
                    print('Вашу карту заблоковано! Зверніться в банк до Брежнева Андрія!')
                    break

    def menu(self):
        choise = int(input(f'{self.first_name}, виберіть дію, яку хочете виконати.\n'
              f'1 - Перевірка балансу, 2 - Зняття готівки, 3 - Поповнення балансу, 4 - Конвертація коштів, 5 - Вихід: '))
        if choise == 1:
            andrii.my_balance()
        if choise == 2:
            andrii.withdraw()
        if choise == 3:
            andrii.deposit()
        if choise == 4:
            andrii.convert()
        if choise == 5:
            andrii.exit()
        if choise < 1 or choise > 5:
            print('Зробіть провильний вибір!')
            andrii.menu()


    def my_balance(self):
        print(f'{self.first_name}, на Вашому балансі\n{round(self.balance, 2)} гривень\n{round(self.usd, 2)} доларів США'
              f'\n{round(self.gbp, 2)} фунтів\n{round(self.euro, 2)} євро')
        andrii.cont()


    def withdraw(self):
        withdr = int(input(f'{self.first_name}, ведіть сумму коштів для зняття: '))
        if withdr > self.balance:
            print(f'{self.first_name}, на вашому балансі недостатньо коштів.')
            andrii.cont()
        else:
            print(f'{self.first_name}, на Вашому балансі залишилось {self.balance - withdr} гривень.')
            andrii.cont()


    def deposit(self):
        bal = int(input(f'{self.first_name}, ведіть сумму, яку хочете покласти на баланс: '))
        self.balance += bal
        print(f'{self.first_name}, на вашому балансі {self.balance} гривень')
        andrii.cont()

    def convert(self):
        conv = int(input(f'{self.first_name}, в яку валюту конвертувати Ваші кошти?\n1 - USD, 2 - GBP, 3 - EUR: '))
        if conv == 1:
            y = float(input(f'{self.first_name}, введіть сумму для конвертаціі: '))
            if y <= self.balance:
                self.usd = y / 42.01
                self.balance -= y
                print(f'Конвертація успішна. На Вашому рахунку {round(self.usd, 2)} доларів США.')
                andrii.cont()
            if y > self.balance:
                print(f'{self.first_name}, на Вашому рахунку недостатньо коштів для конвертації.')
                andrii.cont()
        if conv == 2:
            y = float(input(f'{self.first_name}, введіть сумму для конвертаціі: '))
            if y <= self.balance:
                self.gbp = y / 52.68
                self.balance -= y
                print(f'Конвертація успішна. На Вашому рахунку {round(self.gbp, 2)} фунтів стерлінгів.')
                andrii.cont()
            if y > self.balance:
                print(f'{self.first_name}, на Вашому рахунку недостатньо коштів для конвертації.')
                andrii.cont()
        if conv == 3:
            y = float(input(f'{self.first_name}, введіть сумму для конвертаціі: '))
            if y <= self.balance:
                self.euro = y / 43.81
                self.balance -= y
                print(f'Конвертація успішна. На Вашому рахунку {round(self.euro, 2)} євро.')
                andrii.cont()
            if y > self.balance:
                print(f'{self.first_name}, на Вашому рахунку недостатньо коштів для конвертації.')
                andrii.cont()

    def cont(self):
        x = int(input(f'{self.first_name}, бажаєте продовжити роботу? 1 - Так, 2 - Ні: '))
        if x == 1:
            andrii.menu()
        if x == 2:
            print(f'{self.first_name}, дякуємо за вибір нашого банку!')

    def exit(self):
        print(f'{self.first_name}, дякуємо за вибір нашого банку!')



andrii = Brebank('Andrii', "Brezhnev", 48, '+380671659558', 1111, 0)
andrii.password()

