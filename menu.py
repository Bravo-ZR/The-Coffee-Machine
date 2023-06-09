class Menu:
    def __init__(self)-> None:
        self.menu_card = { 
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "milk": 0,
                    "coffee": 18,
                },
                "cost": 100,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 200,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 250,
            }
        }