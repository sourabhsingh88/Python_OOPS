
class Account :
    def __init__(self , balance):
        self.__balance = balance


    def deposit(self , amount):
        if amount <= 0 :
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self , amount):
        if amount <= 0 :
            raise ValueError("Must Be Positive")
        if amount > self.__balance :
            raise ValueError("No enoung balance")
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance


acc = Account(0)
acc.deposit(5000)
print(acc.balance)
