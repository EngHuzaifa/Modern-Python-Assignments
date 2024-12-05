class Payment:
    def __init__(self, amount: int):
        self.amount:int = amount

    def process_payment(self):
        print(f"Processing payment of {self.amount} using a generic method.")


class CreditCardPayment(Payment):
    def process_payment(self):
        print(f"Processing credit card payment of {self.amount}.")


class PayPalPayment(Payment):
    def process_payment(self):
        print(f"Processing PayPal payment of {self.amount}.")


class BankTransferPayment(Payment):
    def process_payment(self):
        print(f"Processing bank transfer payment of {self.amount}.")


def execute_payments(payments):
    for payment in payments:
        payment.process_payment()


# Create instances of different payment types and execute them
credit_card_payment = CreditCardPayment(1000)
paypal_payment = PayPalPayment(500)
bank_transfer_payment = BankTransferPayment(200)

payments = [credit_card_payment, paypal_payment, bank_transfer_payment]
execute_payments(payments)
