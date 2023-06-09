class MoneyMachine:
    def __init__(self, menu) -> None:
        """
        Initializes a MoneyMachine object.

        Args:
            menu (dict): A dictionary containing the menu items and their details.
        """
        self.profit = 0
        self.menu = menu
        self.drink = ''

    def make_payment(self):
        """
        Processes the payment for the selected drink.

        Returns:
            bool: True if the payment is successful, False otherwise.
        """
        self.payment = int(input('Insert Coins: '))
        self.drink_details = self.menu[self.drink]
        self.drink_cost = self.drink_details['cost']

        if self.payment == self.drink_cost:
            print("Thank you for the payment.")
            return True
        elif self.payment > self.drink_cost:
            change = self.payment - self.drink_cost
            print(f"Thank you for the payment and here is your change of {change}.")
            return True
        else:
            print('Not enough coins, payment refunded.')
            return False
