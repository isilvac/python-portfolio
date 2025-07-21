from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_on = True
coffe_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while machine_is_on:
    action = input(f'What would you like? ({menu.get_items()}): ').lower()
    if action == 'report':
        coffe_machine.report()
        money_machine.report()
    elif action == 'off':
        print("Bye.")
        machine_is_on = False
    else:
        drink = menu.find_drink(action)
        if drink and coffe_machine.is_resource_sufficient(drink):
            cost_of_drink = drink.cost
            if money_machine.make_payment(cost_of_drink):
                coffe_machine.make_coffee(drink)
