class Bank:
    def __init__(self, first_name, last_name, pincode, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.pincode = pincode
        self.balance = balance

    def info(self):
        print(f'{self.first_name} {self.last_name} на Вашому балансі {self.balance} гривень')

    def deposit(self):
        dep = int(input(f'{self.first_name} введіть суму для поповнення: '))
        self.balance += dep
        print(f'{self.first_name}, на Вашому рахунку {self.balance} гривень.')

class MonoBank(Bank):
    def __init__(self, first_name, last_name, pincode, balance, validity):
        super().__init__(first_name, last_name, pincode, balance)
        self.validity = validity

    def validity_period(self):
        print(f'{self.first_name} {self.last_name} Ваша картка дыйсна до {self.validity}')

class PrivatBank(Bank):

    def change_pin(self):
        new_pin = int(input(f'{self.first_name} введіть новий pin-код: '))
        self.pincode = new_pin
        print(f'{self.first_name}, Ващ pin-код змінено на новий {self.pincode}')

class Pumb(Bank):

    def info(self):
        print(f'{self.first_name}, ради вітати Вас в нашому банку!')




mo_bank = MonoBank('Андрій', 'Брежнев', 2222, 1000, '15 квітня 2028')
p_bank = PrivatBank('Андрій', 'Брежнев', 5555, 7000)
pumb = Pumb('Андрій', 'Брежнев', 7777, 15000)

mo_bank.info()
p_bank.info()
pumb.info()
mo_bank.deposit()
p_bank.deposit()
mo_bank.validity_period()
p_bank.change_pin()

