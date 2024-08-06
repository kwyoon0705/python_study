from coffee_machine_data import MENU, resources


# TODO : 1. Print Report.
def print_report(resources_usable):
    print(f"Water : {resources_usable['water']}ml")
    print(f"Milk : {resources_usable['milk']}ml")
    print(f"Coffee : {resources_usable['coffee']}g")


# TODO : 2. Check resources sufficient.
def check_resources(ordered_coffee):
    ingredients = MENU.get(ordered_coffee).get("ingredients")
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, There is not enough {item}.")
            return False
    return True


# TODO : 3. Process coins.
def check_coins():
    print("Please Insert Coins.")
    quarters = float(input("How many quarters? : ")) * 0.25
    dimes = float(input("How many dimes? : ")) * 0.1
    nickels = float(input("How many nickels? : ")) * 0.05
    pennies = float(input("How many pennies? : ")) * 0.01
    inserted_cost = round(quarters + dimes + nickels + pennies, 3)
    print(f"You inserted ${inserted_cost}.")
    return inserted_cost


# TODO : 4. Check transaction successful.
def transaction(inserted_payment, coffee_cost):
    if inserted_payment < coffee_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${inserted_payment-coffee_cost} in change.")
        return True


# TODO : 5. Make Coffee.
def make_coffee(ordered_coffee):
    ingredients = MENU.get(ordered_coffee).get("ingredients")
    for item in ingredients:
        resources[item] -= ingredients[item]
    return True


def supply_resources():
    for item in resources:
        resources[item] += 100


resources = resources
ongoing = True
coffee_list = MENU.keys()

while ongoing:
    order = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if order == "off":
        print("Goodbye.")
        ongoing = False
    if order == "report":
        print_report(resources)
    elif order == "supply":
        supply_resources()
        print("Supply resources.")
    elif order in coffee_list:
        cost = MENU[order]["cost"]
        print(f"You ordered {order}. It's ${cost}.")
        is_enough_resources = check_resources(order)
        if is_enough_resources:
            payment = check_coins()
            if transaction(payment, cost):
                if make_coffee(order):
                    print(f"Here is your {order}")
                    print(resources)
