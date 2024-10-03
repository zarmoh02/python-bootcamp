from data import resources
from data import menu


# todo: report the machine resources
def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    return print(f"water:{water}ml\nmilk:{milk}ml\ncoffee:{coffee}g\nmoney:${money}")


# todo: check if resources is sufficient
def check_sufficient(order_ingeredient):
    for item in order_ingeredient:
        if int(order_ingeredient[item]) >= int(resources[item]):
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


# todo: process coins
# todo: see if transaction was successful?
def pay(price):
    print("please insert coins:")
    quarters = int(input("quarters:"))
    dime = int(input("dime:"))
    nickle = int(input("nickle:"))
    penny = int(input("penny:"))
    total_pay = quarters * 0.25 + dime * 0.1 + nickle * 0.05 + penny * 0.01
    if total_pay < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources["money"] += price
        change = round(total_pay - price, 2)
        print(f"transaction successful, Here is ${change} dollars in change.")
        return True


def make_coffee(ingredient):
    for item in ingredient:
        resources[item] -= int(ingredient[item])
    print("here is your drink.enjoy it!")


# todo: ask user their order, show it after every loop
machine_on = True
while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    # todo: turn off machine by typing off
    if order == "off":
        machine_on = False
        break
    elif order == "report":
        report()
    else:
        drink = menu[order]
        if check_sufficient(drink["ingredients"]):
            # todo: make coffee
            if pay(drink["cost"]):
                make_coffee(drink["ingredients"])
