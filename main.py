from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo
import time
import os

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


menu = Menu()
coffee_machine = CoffeeMaker(menu.menu_card)
money_machine = MoneyMachine(menu.menu_card)

exit_program = False

while not exit_program:
    print(logo)
    
    ask = input('What do you want (espresso, latte, cappuccino): \n')
    coffee_machine.drink = ask
    money_machine.drink = ask
    time.sleep(1)
    
    if ask == 'report':
        print(coffee_machine.report())
        
    elif ask == 'exit':
        print('Exiting Program.')
        exit_program = True
        
    elif coffee_machine.find_drink():
        
        if coffee_machine.resource_sufficient():
            if money_machine.make_payment():    
                coffee_machine.make_coffee()
        else:
            print('Not enough resources.')
    time.sleep(2)
    clear()