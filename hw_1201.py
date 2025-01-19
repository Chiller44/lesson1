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
            self.transaction.append(f'{bal} {self.currency} - {comment}')
            print(f'Поточний баланс {self.initial_balance} {self.currency}')
            print(self.transaction)
        else:
            if isinstance(bal,(int, float)):
                self.initial_balance +=bal
                self.transaction.append(f'Поповнення рахунку на {bal} {self.currency}')
                print(f'{self.name}: поточний баланс {self.initial_balance} {self.currency}')
                print(self.transaction)
            if isinstance(bal, list):
                for i in bal:
                    self.initial_balance += i
                    self.transaction.append(f'Поповнення рахунку на {i} {self.currency}')
                print(f'{self.name}: поточний баланс - {self.initial_balance} {self.currency}')
                print(self.transaction)

    def withdraw(self, w_draw, comment = None):
        if isinstance(w_draw, (float, int)) and comment == None:
            if w_draw <= self.initial_balance:
                self.initial_balance -= w_draw
                self.transaction.append(f'Переказ коштів {w_draw} {self.currency}')
                print(f'Поточний баланс {self.initial_balance} {self.currency}')
            else:
                print(f'Недостатньо коштів на рахунку')
        if isinstance(w_draw, list):
            if sum(w_draw) <= self.initial_balance:
                for i in w_draw:
                    self.initial_balance -= i
                    self.transaction.append(f'Зняття коштів {i} {self.currency}')
                print(f'Поточний баланс {self.initial_balance} {self.currency}')
            else:
                print(f'Недостатньо коштів на рахунку')
        if comment == 'USD':
            if w_draw * 42.29 < self.initial_balance:
                self.initial_balance -= w_draw * 42.29
                print(f'Поточний баланс {self.initial_balance} {self.currency}')
                self.transaction.append(f'Зняття коштів {w_draw} {comment}')
            else:
                print(f'Недостатньо коштів на рахунку')

    def transfer(self, transf, to_account = None, comment = None):
        if transf <= self.initial_balance:
            if comment == None and to_account == None:
                self.initial_balance -= transf
                self.transaction.append(f'Переказ коштів {transf} {self.currency}')
            if to_account != None and comment == None:
                self.initial_balance -= transf
                to_account.initial_balance += transf
                self.transaction.append(f'Переказ коштів {transf} {self.currency} {to_account.name}')
                to_account.transaction.append(f'Переказ коштів {transf} {self.currency} від {self.name}')
            if to_account != None and comment != None:
                self.initial_balance -= transf
                to_account.initial_balance += transf
                self.transaction.append(f'Переказ коштів {transf} {self.currency} {to_account.name} - {comment}')
                to_account.transaction.append(f'Переказ коштів {transf} {self.currency} від {self.name} - {comment}')
        else:
            print(f'Недостатньо коштів на рахунку')

    def get_account_info(self, detailed = None, as_dict = None):
        klients = {}
        if detailed == None and as_dict == None:
            print(f'{self.name}, баланс {self.initial_balance} {self.currency}')
        if detailed == True:
            print(f'{self.name}, {self.initial_balance} {self.currency}, {self.transaction}, кількість транзакцій - {len(self.transaction)}')
        if as_dict == True:
            klients = {self.name: [self.initial_balance, self.currency, self.transaction]}
            print(klients)

class PremiumAccount(Bancaccount):

    def deposit(self, bal, comment = None):
        if comment != None:
            self.initial_balance += bal * 1.01
            self.transaction.append(f'{bal} {self.currency} - {comment}, бонус {round(bal/100, 2)} гривень')
            print(f'Поточний баланс {self.initial_balance} {self.currency}')
            print(self.transaction)
        else:
            if isinstance(bal,(int, float)):
                self.initial_balance +=bal * 1.01
                self.transaction.append(f'Поповнення рахунку на {bal} {self.currency}, бонус {round(bal/100, 2)} гривень')
                print(f'{self.name}: поточний баланс {self.initial_balance} {self.currency}')
                print(self.transaction)
            if isinstance(bal, list):
                for i in bal:
                    self.initial_balance += i * 1.01
                    self.transaction.append(f'Поповнення рахунку на {i} {self.currency}, бонус {round(i/100, 2)} гривень')
                print(f'{self.name}: поточний баланс - {self.initial_balance} {self.currency}')
                print(self.transaction)

    def withdraw(self, w_draw, comment = None):
        if isinstance(w_draw, (float, int)) and comment == None:
            if w_draw <= self.initial_balance + 1000:
                self.initial_balance -= w_draw
                self.transaction.append(f'Переказ коштів {w_draw} {self.currency}')
                print(f'Поточний баланс {self.initial_balance} {self.currency}')
            else:
                print(f'Недостатньо коштів на рахунку')
        if isinstance(w_draw, list):
            if sum(w_draw) <= self.initial_balance + 1000:
                for i in w_draw:
                    self.initial_balance -= i
                    self.transaction.append(f'Зняття коштів {i} {self.currency}')
                print(f'Поточний баланс {self.initial_balance} {self.currency}')
            else:
                print(f'Недостатньо коштів на рахунку')
        if comment == 'USD':
            if w_draw * 42.29 < self.initial_balance + 1000:
                self.initial_balance -= w_draw * 42.29
                print(f'Поточний баланс {self.initial_balance} {self.currency}')
                self.transaction.append(f'Зняття коштів {w_draw} {comment}')
            else:
                print(f'Недостатньо коштів на рахунку')

    def transfer(self, transf, to_account = None, comment = None):
        if transf * 1.005 <= self.initial_balance + 1000:
            if comment == None and to_account == None:
                self.initial_balance -= (transf + (transf/100 * .5))
                self.transaction.append(f'Переказ коштів {transf} {self.currency}')
            if to_account != None and comment == None:
                self.initial_balance -= (transf + (transf/100 * .5))
                to_account.initial_balance += transf
                self.transaction.append(f'Переказ коштів {transf} {self.currency} {to_account.name}, {round((transf/100 * .5), 2)} {self.currency}- комісія банку')
                to_account.transaction.append(f'Переказ коштів {transf} {self.currency} від {self.name}')
            if to_account != None and comment != None:
                self.initial_balance -= (transf + (transf/100 * .5))
                to_account.initial_balance += transf
                self.transaction.append(f'Переказ коштів {transf} {self.currency} {to_account.name} - {comment}, {round((transf/100 * .5), 2)} {self.currency} - комісія банку')
                to_account.transaction.append(f'Переказ коштів {transf} {self.currency} від {self.name} - {comment}')
                print(self.transaction)
        else:
            print(f'Недостатньо коштів на рахунку')










o1 = Bancaccount("Andrii")
o2 = Bancaccount('Oleh', 1000)
o3 = Bancaccount('Ihor', 1000, 'UAH')
o4 = PremiumAccount('Nadiia', 6000, 'UAH')

print(o4)
o4.transfer(3000, o2, 'в борг')
o2.get_account_info(False, True)
o4.get_account_info(True, True)

