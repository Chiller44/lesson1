"""
Умови:
1	Створіть абстрактний клас BankAccount, який містить:
    ◦	Поле balance (баланс).
    ◦	Абстрактний метод deposit(amount), який додає кошти на рахунок.
    ◦	Абстрактний метод withdraw(amount), який знімає кошти з рахунку.
    ◦	Метод get_balance(), який повертає поточний баланс.
2	Реалізуйте підкласи:
    ◦	SavingsAccount (ощадний рахунок), де:
    ▪	Не можна знімати більше, ніж є на рахунку.
    ▪	Додається річний відсоток (наприклад, 5%) через метод apply_interest().
    ◦	CreditAccount (кредитний рахунок), де:
    ▪	Можна піти в мінус до певного credit_limit.
    ▪	Якщо баланс негативний, знімається комісія (наприклад, 2% від боргу).
3	Створіть екземпляри SavingsAccount та CreditAccount, проведіть кілька операцій і виведіть результати.

Додаткові ускладнення:
    •	Додати логування всіх транзакцій.
    •	Реалізувати можливість переказу коштів між рахунками.
    •	Додати ще один тип рахунку, наприклад, депозитний із фіксованим

"""


from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance = 0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, bal):
        super().__init__(bal)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print('Недостатньо коштів для зняття!')
        else:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        print(f'На Вашому рахунку {self.balance}')

    def apply_interest(self, percent):
        #річний відсоток з виплатою щомісяця
        if percent < 0:
            print("Відсоткова ставка не може бути від'ємною!")
        else:
            self.balance += self.balance * percent/1200

    def transfer(self, amount, to_account):
        if amount <= self.balance:
            self.balance -= amount
            to_account.balance += amount
        else:
            print('Недостатньо коштів для переводу!')

class CreditAccount(BankAccount):
    def __init__(self, bal, credit_limit=500):
        super().__init__(bal)
        self.credit_limit = credit_limit


    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        elif self.balance + self.credit_limit >= amount > self.balance:
            self.balance -= amount
            print('Ви скористались кредитними коштами!')
        else:
            print('Транзакція неможлива. Сума для зняття більша за кредитний ліміт!')
        return self.balance

    def get_balance(self, percent):
        if self.balance > 0:
            print(f'На Вашому рахунку {self.balance}')
        else:
            self.balance -= self.balance * percent / 1200
            print(f'З Вас стягується комісія в розмірі {percent}% річних.')
            print(f'На Вашому рахунку {abs(round(self.balance, 2))} доступних кредитних коштів')

    def transfer(self, amount, to_account):
        if amount <= self.balance + self.credit_limit:
            self.balance -= amount
            to_account.balance += amount
        else:
            print('Недостатньо коштів для переводу!')


Oleh = SavingsAccount(500)
Andrii = SavingsAccount(100)

Anna = CreditAccount(200)
Nadiia = CreditAccount(400)

Oleh.transfer(5000, Anna)
Anna.deposit(100)
Anna.transfer(700, Nadiia)
#Anna.withdraw(700)
Anna.get_balance(2)
Nadiia.get_balance(2)

