from abc import ABC, abstractmethod


# --------------------------------
# Abstract Base Class
# --------------------------------

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


# --------------------------------
# Credit Card Payment
# --------------------------------

class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid using Credit Card")

    def refund(self, amount):
        print(f"₹{amount} refunded to Credit Card")


# --------------------------------
# UPI Payment
# --------------------------------

class UPIPayment(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid using UPI")

    def refund(self, amount):
        print(f"₹{amount} refunded to UPI")


# --------------------------------
# PayPal Payment
# --------------------------------

class PayPalPayment(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid using PayPal")

    def refund(self, amount):
        print(f"₹{amount} refunded to PayPal")


# --------------------------------
# Cash Payment
# --------------------------------

class CashPayment:

    def pay(self, amount):
        print(f"₹{amount} paid using Cash")

    def refund(self, amount):
        print(f"₹{amount} refunded in Cash")


# --------------------------------
# Common Functions
# --------------------------------

def process_payment(payment, amount):
    payment.pay(amount)


def process_refund(payment, amount):
    payment.refund(amount)


# --------------------------------
# Creating Objects
# --------------------------------

credit_card = CreditCardPayment()
upi = UPIPayment()
paypal = PayPalPayment()
cash = CashPayment()


# --------------------------------
# Runtime Polymorphism
# --------------------------------

process_payment(credit_card, 1000)
process_payment(upi, 2000)
process_payment(paypal, 3000)

# Duck typing
process_payment(cash, 500)


# --------------------------------
# Refund
# --------------------------------

process_refund(credit_card, 200)
process_refund(upi, 300)
process_refund(paypal, 400)

# Duck typing
process_refund(cash, 100)