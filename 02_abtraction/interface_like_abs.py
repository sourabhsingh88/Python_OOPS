from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

# Interface = abstract class with only abstract methods
# Abstract class = abstract + concrete methods
class UpiPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class CardPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} using Card")


payment = UpiPayment()
payment.pay(500)
payment = CardPayment()
payment.pay(1000)
