from abc import ABC , abstractmethod

class Account(ABC) :
    def __init__(self , balance):
        self._bal = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


    @property
    @abstractmethod
    def balance(self):
        pass

class Saving_Account(Account) :

    # def __init__(self, balance):
    #     self.__bal = balance

    def  __init__(self , balance):
        super().__init__(balance)

    def deposit(self, amount):
        if amount <=0 :
            raise ValueError("Cant be negative")
        self._bal += amount

    def withdraw(self, amount):
        if amount <=0 :
            raise ValueError("Cant be negative")
        if amount > self._bal :
            raise ValueError("insufficient Balance in account")
        self._bal -= amount

    @property
    def balance(self):
        return self._bal

acc= Saving_Account(0)

acc.deposit(1000)
print(acc.balance)

acc.withdraw(1000)
print(acc.balance)
acc.withdraw(1000) # Error "insuff"
print(acc.balance)