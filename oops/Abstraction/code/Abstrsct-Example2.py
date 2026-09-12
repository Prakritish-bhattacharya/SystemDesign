from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"paid ${amount} using UPI")

# Instance creation of UPIPayment class
upi = UPIPayment()
upi.pay(500)

#  Instance creation of CreditCardPayment class
credit_card = CreditCardPayment()
credit_card.pay(1000)