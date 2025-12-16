from abc import ABC , abstractmethod
# Create Account class with 2 attribute -  balance and account nmber
# Create methods for debt , credit and printing balance


class Bank(ABC) :
    def __init__(self , bal, acc_no ):
        self.acc_no = acc_no
        self.bal = bal
    @abstractmethod
    def debt(self):
        pass
    @abstractmethod
    def cred(self):
        pass
    def print_bal(self):
        print(f"current balance is {self.bal}")
class Account(Bank) :
    def debt(self , Amount):
        self.bal -= Amount
        print(f"amount debit {Amount}")
        self.print_bal()

    def cred(self, Amount):
        self.bal += Amount
        print(f"amount credit {Amount}")
        self.print_bal()
# -------------------------------------------
acc = Account(5000 , 1234)
print(f"Your Account Number is {acc.acc_no}")
print(f"Your Account Have balance {acc.bal} only")
acc.cred(500)
acc.debt(1000)
acc.print_bal()