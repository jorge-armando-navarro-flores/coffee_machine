from machine_data import MENU, resources, coins

machine_money = 0


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${machine_money}")


def resources_sufficient(coffee_ingredients):
    for key in resources.keys():
        if key in coffee_ingredients:
            if resources[key] < coffee_ingredients[key]:
                print(f"Sorry there is not enough {key}.")
                return False
    return True


def process_coins():
    inserted_money = 0
    for key in coins.keys():
        inserted_coins = int(input(f"how many {key}?: "))
        inserted_money += coins[key] * inserted_coins
    return inserted_money


def transaction_successful(inserted_money, coffee_price):
    if inserted_money < coffee_price:
        return False
    else:
        return True


def make_coffee(coffee_ingredients):
    for key in resources.keys():
        if key in coffee_ingredients:
            resources[key] -= coffee_ingredients[key]


order = input("What would you like? (espresso/latte/cappuccino): ")


while order != "off":

    if order == "report":
        print_report()
    else:
        coffee = MENU[order]
        if resources_sufficient(coffee["ingredients"]):
            print("Please insert coins.")
            user_money = process_coins()
            if transaction_successful(user_money, coffee["cost"]):
                make_coffee(coffee["ingredients"])
                machine_money += coffee["cost"]
                user_change = round(user_money - coffee["cost"], 2)
                print(f"Here is ${user_change} in change.")
                print(f"Here is your {order} ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")

    order = input("What would you like? (espresso/latte/cappuccino): ")
