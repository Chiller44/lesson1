


class Bancaccount:
    def __init__(self, name, initial_balance=0, currency='UAH'):
        self.name = name
        self.initial_balance = initial_balance
        self.currency = currency
        self.transaction = []

    def __str__(self):
        return f'{self.name} {self.initial_balance} {self.currency}'

    def deposit(self, bal, comment = None):
        if comment != None:
            self.initial_balance += bal
            self.transaction.append(f'{bal} - {comment}')
            print(self.transaction)
            print(f'Поточний баланс {self.initial_balance} {self.currency}')
        else:
            if isinstance(bal,(int, float)):
                self.initial_balance +=bal
                self.transaction.append(f'Поповнення рахунку на {bal} {self.currency}')
                print(self.transaction)
                print(f'{self.name}: поточний баланс {self.initial_balance} {self.currency}')
            if isinstance(bal, list):
                for i in bal:
                    self.initial_balance += i
                    self.transaction.append(f'Поповнення рахунку на {i} {self.currency}')
                    print(self.transaction)
                    print(f'{self.name}: поточний баланс - {self.initial_balance} {self.currency}')

    def withdraw(self, w_draw, comment = None):
        if comment == 'USD':
            if w_draw * 42.29 < self.initial_balance:
                self.initial_balance -= w_draw * 42.29
                print(f'Поточний баланс {self.initial_balance} {self.currency}')
            else:
                print(f'Недостатньо коштів на рахунку')
        else:
            if isinstance(w_draw, (int, float)):
                self.initial_balance -= w_draw
                print(f'Поточний баланс {self.initial_balance} {self.currency}')
            if isinstance(w_draw, list):
                for i in w_draw:
                    self.initial_balance -= i
                    self.transaction.append(f'Знаття коштів на {i} {self.currency}')
                print(self.transaction)
                print(f'Поточний баланс {self.initial_balance} {self.currency}')


    def transfer(self, transf, to_account = None, comment = None):
        if transf > self.initial_balance:
            print('Недостатньо коштів на балансі для переказу')
        else:
            self.initial_balance -= transf
            self.transaction.append(f'{transf} {comment}')
            if to_account:
                to_account.initial_balance += transf
            print(self.transaction)
            print(f'{self.name} поточний баланс {self.initial_balance} {self.currency}')
            if comment != None:
                print(f'{self.transaction}')
            if to_account != None:
                print(f'{to_account.name} поточний баланс {to_account.initial_balance} гривень')

    def get_account_info(self, detailed = None, as_dict = None):
        klients = {}
        if detailed == None and as_dict == None:
            print(f'{self.name}, баланс {self.initial_balance} гривень')
        if detailed == True:
            print(f'{self.name}, {self.initial_balance} гривень, {self.currency}, {self.transaction}')
        if as_dict == True:
            klients = {self.name: [self.initial_balance, self.currency, self.transaction]}
            print(klients)


class PremiumAccount(Bancaccount):

    def deposit(self, bal, comment = None):
        if comment != None:
            self.initial_balance += bal * 1.01
            self.transaction.append(f'{bal} - {comment}')
            print(f'Поточний баланс {round(self.initial_balance), 2} гривень')
            print(self.transaction)
        else:
            if isinstance(bal,(int, float)):
                self.initial_balance +=bal * 1.01
                self.transaction.append(f'Поповнення рахунку на {bal} гривень, бонус {round(bal/100, 2)} гривень')
                print(f'{self.name}: поточний баланс {round(self.initial_balance, 2)} гривень')
                print(self.transaction)
            if isinstance(bal, list):
                for i in bal:
                    self.initial_balance += i * 1.01
                    self.transaction.append(f'Поповнення рахунку на {i} гривень, бонус {round(i/100, 2)} гривень')
                    print(f'{self.name}: поточний баланс - {round(self.initial_balance, 2)} гривень')
                    print(self.transaction)

    def withdraw(self, w_draw, comment = None):
        if comment == self.currency:
            if w_draw * 42.29 <= self.initial_balance + 1000:
                self.initial_balance -= w_draw * 42.29
                print(f'Поточний баланс {round(self.initial_balance, 2)} гривень')
            else:
                print(f'Недостатньо коштів на рахунку')
        else:
            if isinstance(w_draw, (int, float)):
                self.initial_balance -= w_draw
                print(f'Поточний баланс {round(self.initial_balance, 2)} гривень')
            if isinstance(w_draw, list):
                for i in w_draw:
                    self.initial_balance -= i
                print(f'Поточний баланс {round(self.initial_balance, 2)} гривень')
        if self.initial_balance < 0:
            print(f'{self.name}, звкрніть увагу, Вам потрібно погасити борг.')

    def transfer(self, transf, to_account=None, comment=None):
        if transf > self.initial_balance:
            print('Недостатньо коштів на балансі для переказу')
        else:
            self.initial_balance -= (transf + transf * 0.005)
            self.transaction.append(f'{transf} {comment}, {round(transf * 0.005, 2)} гривень комісія банку')
            if to_account:
                to_account.initial_balance += transf
            print(f'{self.name} поточний баланс {round(self.initial_balance, 2)} гривень')
            if comment != None:
                print(f'{self.transaction}')
            if to_account != None:
                print(f'{to_account.name} поточний баланс {round(to_account.initial_balance, 2)} гривень')







o1 = Bancaccount("Andrii")
o2 = Bancaccount('Oleh', 1000)
o3 = Bancaccount('Ihor', 1000, 'UAH')
o4 = PremiumAccount('Віктор', 10000)
o5 = PremiumAccount('Катерина', 20000)

o3.deposit(5000)
o3.withdraw([1000, 2000])
o3.transfer(2000, o5)
o3.get_account_info(False, True)
