class BankAccount:
    def __init__ (self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        self.balance +=200

    def withdraw(self):
        if self.balance - 300 < 0:
            print('Недостатньо коштів')
        else:
            self.balance -=300


