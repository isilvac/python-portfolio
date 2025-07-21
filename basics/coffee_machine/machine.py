from data.main import resources, MENU

machine_is_on = True
money = {
    "pennies": 0,
    "nickles": 0,
    "dimes": 0,
    "quarters": 0
}


def get_money():
    return money["pennies"] * 0.01 + money["nickles"] * 0.05 + money["dimes"] * 0.1 + money["quarters"] * 0.25


def get_report():
    for element in resources:
        if element == 'coffee':
            print(f"{element.capitalize()}: {resources[element]}g")
        else:
            # Milk and Water
            print(f"{element.capitalize()}: {resources[element]}ml")
    print(f"Money: ${'${:,.2f}'.format(get_money())}")


def has_resources(ingredients):
    """Validates if the resources are enough to prepare beverage"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def add_coins(penny, nickle, dime, quarter):
    money["pennies"] += penny
    money["nickles"] += nickle
    money["dimes"] += dime
    money["quarters"] += quarter


def remove_coins(penny, nickle, dime, quarter):
    money["pennies"] -= penny
    money["nickles"] -= nickle
    money["dimes"] -= dime
    money["quarters"] -= quarter


def refund(refund_amount):
    """" Based on the amount to be refunded, it returns the coins from larger to smaller """
    # print(f"To refund: ${'${:,.2f}'.format(refund_amount)}")
    quarters_to_remove = min(money["quarters"], int(refund_amount / 0.25))
    refund_amount -= quarters_to_remove * 0.25

    dimes_to_remove = min(money["dimes"], int(refund_amount / 0.1))
    refund_amount -= dimes_to_remove * 0.1

    nickles_to_remove = min(money["nickles"], int(refund_amount / 0.05))
    refund_amount -= nickles_to_remove * 0.05

    pennies_to_remove = min(money["pennies"], int(refund_amount / 0.01))
    refund_amount -= pennies_to_remove * 0.01

    remove_coins(pennies_to_remove, nickles_to_remove, dimes_to_remove, quarters_to_remove)
    refunded = quarters_to_remove * 0.25 + dimes_to_remove * 0.1 + nickles_to_remove * 0.05 + pennies_to_remove * 0.01
    print(f"Here is ${'{:,.2f}'.format(refunded)} in change")
    # print(f"Here is Q:{quarters_to_remove} D:{dimes_to_remove} N:{nickles_to_remove} P:{pennies_to_remove}")
    if float('{:,.2f}'.format(refund_amount)) > 0:
        print(f"I owe you the rest (${refund_amount}). Sorry.")


def use_coins(beverage):
    cost = MENU[beverage]["cost"]
    print(f"The {beverage} costs ${'${:,.2f}'.format(cost)}. Please insert coins:")
    penny = int(input("Pennies: "))
    nickle = int(input("Nickles: "))
    dime = int(input("Dimes: "))
    quarter = int(input("Quarters: "))
    total_coins = penny * 0.01 + nickle * 0.05 + dime * 0.1 + quarter * 0.25
    if total_coins < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        add_coins(penny, nickle, dime, quarter)
        refundable = total_coins - cost
        if refundable > 0:
            refund(refundable)
    return True


def prepare_coffee(drink_ingredients):
    for item in resources:
        resources[item] -= drink_ingredients.get(item, 0)


def run_machine():
    global machine_is_on
    while machine_is_on:
        action = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if action == 'report':
            get_report()
        elif action == 'off':
            print("Bye.")
            machine_is_on = False
        else:
            found = False
            for drink in MENU:
                if action == drink:
                    found = True
                    if has_resources(MENU[drink]["ingredients"]):
                        if use_coins(action):
                            prepare_coffee(MENU[drink]["ingredients"])
                            print(f"Here is your {drink}.☕️ Enjoy!")
            if not found:
                print("Option not available")


run_machine()
