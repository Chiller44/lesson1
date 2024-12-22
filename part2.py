from uuid import uuid4

x = str(uuid4())

class UserBank:
    def __init__(self, name, age, logPhone):
        self.__name = name
        self.__age = age
        self.__guid = str(uuid4())
        self.__balance = 0
        self.__loginPhone = logPhone
        self.__password = self.getRassword()

    def changePass(self):
            answ = input('Enter password: ')
            if answ == self.__password:
                while True:
                    new_pass1 = input('Enter new password: ')
                    new_pass2 = input ('Confirm u password')
                    if new_pass1 == new_pass2:
                        self.__password = new_pass1
                        break

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = newName

    @property
    def loginPhone(self):
        return self.__loginPhone
    @loginPhone.setter
    def loginPhone(self, newNumber):
        x = ""
        x.isalpha()
        if newNumber.lower().startwith('+380') and not newNumber.isalpha() and len(newNumber) == 13:
            self.__loginPhone = newNumber
        else:
            print('Некорректний номер')

    @property
    def balance(self):
        return




    def getRassword(self):
        password = str (uuid4())
        return password[0:8]

    def showInfo(self):
        print(f'user id = {self.__guid}')

tom = UserBank('Tom', 22, '+38067111111')
tom.showInfo()
tom.changePass()

