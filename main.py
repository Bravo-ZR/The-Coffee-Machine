from logo import logo
import os
from resources import resources, MENU
import time

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def report():
    """Generates a report of the current available resources."""
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    report = f'''
    Current resources available:
    Water : {water}
    Milk  : {milk}
    Coffee: {coffee}
    '''
    return report


exit_program = False

while not exit_program:
    
    print(logo)
    
    ask = str(input('What do you want (espresso, latte, cappuccino): \n'))
    
    if ask == 'report' or ask == 'exit':
        
        password = 'ADMIN'
        pass_input = input('Password: ')
        
        if pass_input == password:
            if ask == 'report':
                print(report())
                time.sleep(5)
                clear()
                continue
            elif ask == 'exit':
                exit_program = True
                print("/////Turning off/////")
                time.sleep(2)
                continue

    item = MENU.get(ask)
    
#==============================Processing Part============================================#
    if item:
        ingredients = item['ingredients']
        
        def check(ingredients=ingredients):
            """Checks if there are sufficient resources to make the selected coffee."""
            global resources
            resource_sufficient = True
            if resources['water'] < ingredients.get('water', 0):
                resource_sufficient = False
            elif resources['milk'] < ingredients.get('milk', 0):
                resource_sufficient = False
            elif resources['coffee'] < ingredients.get('coffee', 0):
                resource_sufficient = False
            else:
                resource_sufficient = True
            return resource_sufficient
        
        
        if check():
            def resource_taken():
                """Deducts the required resources for the selected coffee from the available resources."""
                global resources
                global ingredients
                item_req_water = ingredients.get('water', 0)
                item_req_milk = ingredients.get('milk', 0)
                item_req_coffee = ingredients.get('coffee', 0)
                resources['water'] -= item_req_water
                resources['milk'] -= item_req_milk
                resources['coffee'] -= item_req_coffee

            def coffee():
                """Processes the selected coffee order."""
                insert = int(input('Insert coins: '))
                cost = item['cost']
                time.sleep(2)

                if insert > cost:
                    change = insert - cost
                    print(f"Here's your {ask} and change of {change}.")
                    resource_taken()
                elif insert == cost:
                    print(f"Here's your {ask}.")
                    resource_taken()
                else:
                    print("Sorry, you didn't input the correct amount. Money refunded.")
                time.sleep(5)
                clear()

            coffee()
        else:
            print("Not enough resources available.")
    else:
        print("Sorry, you didn't correctly input what you want.")
