class CoffeeMaker:
    def __init__(self, menu) -> None:
        """
        Initializes a CoffeeMaker object.

        Args:
            menu (dict): A dictionary containing the menu items and their details.
        """
        self.drink = ''
        self.menu = menu
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        
    def find_drink(self):
        """
        Checks if the specified drink exists in the menu.

        Returns:
            bool: True if the drink exists, False otherwise.
        """
        self.drink_confirmed = None
        for i in self.menu:
            if self.drink == i:
                self.drink_confirmed = self.drink
                return True
        if self.drink_confirmed is None:
            print("That drink doesn't exist.")
            return False

    def make_coffee(self):
        """
        Makes the specified drink and updates the resources accordingly.
        """
        self.drink_details = self.menu[self.drink]
        self.ingredients = self.drink_details['ingredients']
        print(f'Here is your {self.drink}.')
        self.resources['water'] -= self.ingredients['water']
        self.resources['milk'] -= self.ingredients['milk']
        self.resources['coffee'] -= self.ingredients['coffee']

    def report(self):
        """
        Generates a report of the current available resources.

        Returns:
            str: A formatted string representing the resource report.
        """
        water = self.resources['water']
        milk = self.resources['milk']
        coffee = self.resources['coffee']
        report = f'''
        Current resources available:
        Water : {water}
        Milk  : {milk}
        Coffee: {coffee}
        '''
        return report

    def resource_sufficient(self):
        """
        Checks if there are sufficient resources to make the specified drink.

        Returns:
            bool: True if resources are sufficient, False otherwise.
        """
        self.drink_details = self.menu[self.drink]
        self.ingredients = self.drink_details['ingredients']
        if (
            self.resources['water'] < self.ingredients['water']
            or self.resources['milk'] < self.ingredients['milk']
            or self.resources['coffee'] < self.ingredients['coffee']
        ):
            return False
        else:
            return True
