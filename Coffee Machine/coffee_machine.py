from data import MENU

water = 500
milk = 300
coffee = 200


def report():
    return f" Water = {water} \n Milk = {milk} \n Coffee = {coffee}"


def sufficient_resource(choice):
    if water < MENU[choice]["ingredients"]["water"]:
        return "Sorry there is no enough Water."
    elif milk < MENU[choice]["ingredients"]["milk"]:
        return "Sorry there is no enough MIlk."
    elif coffee < MENU[choice]["ingredients"]["coffee"]:
        return "Sorry there is no enough Coffee"
    else:
        return "okay"


def coins(choice):
    quarters = int(input("How many Quarters? : "))
    dimes = int(input("How many Dimes ? : "))
    nickles = int(input("How many Nickles ? : "))
    pennies = int(input("How many Pennies ? :"))

    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

    if total >= MENU[choice]["cost"]:
        change = (total - MENU[choice]["cost"])
        rounded_change = format(change, ".2f")
        print(f"Here is your ${rounded_change} in change.")
        print(f"Here your {choice} ☕. Enjoy!")
        return "done"
    else:
        print("Sorry that's not enough money . Money refunded.")
        return "refunded"


def update_resource(choice):
    global water
    global milk
    global coffee
    water -= MENU[choice]["ingredients"]["water"]
    milk -= MENU[choice]["ingredients"]["milk"]
    coffee -= MENU[choice]["ingredients"]["coffee"]


while True:
    choice = input("What would you like ? (Espresso/Latte/Cappuccino) : ").lower()
    if choice == "report":
        print(report())
    else:
        outcome = sufficient_resource(choice)
        if outcome == "okay":
            print("Please insert coins.")
            output = coins(choice)
            if output == "done":
                update_resource(choice)
        else:
            print(outcome)



