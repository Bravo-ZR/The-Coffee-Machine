class MoneyMachine:
    def __init__(self, menu) -> None:
        self.profit = 0
        self.menu = menu
        self.drink = ''
    def make_payment(self):
        self.payment = int(input('Insert Coins: '))
        self.drink_detials= self.menu[self.drink]
        self.drink_cost= self.drink_detials['cost']
        if self.payment == self.drink_cost:
            print("Thank you for the payment.")
            return True
        elif self.payment > self.drink_cost:
            print(f"Thank you for the payment and here is your change of {self.payment - self.drink_cost}")
            return True
        else:
            print('Not enough, coins refunded.')
            return False