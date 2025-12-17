class Account :
    def __init__(self , balance):
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount
        print(self.balance)

acc =  Account(1000)
# acc.balance = -5000  #can`t
print(acc.balance)
acc.deposit(1000)
acc.deposit(-10000) # can not
# for this we use encapsultion
