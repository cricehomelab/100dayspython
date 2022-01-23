"""

This program is supposed to simulate the functionalities of a coffee machine.
Features:
    1. Makes 3 flavors of coffee: Espresso, Latte, and Cappuccino
    2. Coin operated

Functionality requirements:
    1. Print Report - to tell us what resources are present.
    2. Check for sufficient resources when a drink is ordered.
        - Keep track of what resources are available.
    3. Process coins
        - know what coins are worth
        - be able to calculate the total of the coins inserted.
    4. Check for successful transaction
        - Need to be able to compare against what the cost of a drink is
        - refund if not enough coins are inserted
        - process the order if enough is inserted.

Those are the requirements that were gone over in the video there was a separate pdf of the requirements that are more
granular will be creating at To Do list with the IDE, and will code from there using the detailed list.

As a bonus I added an ASCII art logo and function to refill the coffee machine, the refill is mostly for testing
purposes.

"""
from D15_CoffeeArt import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# a. check response to decide what to do next.
# b. this response should show every time an action has been completed.
def coffee_machine():
    """main loop to keep the coffee machine running."""
    running = True
    while running:
        print(logo)
        choice = input("What would you like? (espresso/latte/cappuccino):")
        # TODO: 2 Turn off the coffee machine when the "off" prompt is entered.
        if choice == "off":
            break
        elif choice == "report":
            print_report()
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            have_resources = check_resources(choice)
            if have_resources:
                print(f"Your choice of {choice} will cost you, ${round(MENU[choice]['cost'], 2)}")
                payment = complete_transaction(MENU[choice]["cost"], get_money())
                if payment:
                    make_coffee(MENU[choice]["ingredients"])
                    print(f"Here is your {choice}. Be careful it may be hot!")
            else:
                print("not enough resources.")
        elif choice == "refill":
            refill()
        else:
            print("not a valid choice.")


# TODO: 3 Print a report
# a. When a user enters "report" to the prompt a report should be generated should look something like this.
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.15
def print_report():
    """prints a report of the available resources."""
    for item in resources:
        print(f"{item} : {resources[item]}")


# TODO: 4 Check for sufficient resources.
# a. When a user chooses a drink the program should check the resources and make sure there are enough resources.
# b. If there are not enough of a resource(s) the program should display what there is not enough of.
def check_resources(choice):
    """Checks the resources against the user's choice and returns a boolean value depending upon if all ingredients are
    in stock. True is in stock, False means one or more ingredients are out of stock. """
    ingredients = MENU[choice]['ingredients']
    num_ingredients = len(MENU[choice]['ingredients'])
    count = 0
    for item in ingredients:
        if resources[item] > ingredients[item]:
            count += 1
        else:
            print(f"there is not enough {item} to make {choice}.")
    if count == num_ingredients:
        return True
    else:
        return False


# TODO: 5 Process coins
# a. Calculate the value of the coins inserted (need a prompt to get coins inserted)
# b. Return the total value of the coins.
def get_money():
    """asks the user to insert coins calculates how much money that is and returns that value."""
    coins = {'quarters': 0.25, 'dimes': 0.10, 'nickels': 0.05, 'pennies': 0.01}
    money = 0.0
    for coin in coins:
        inserted = int(input(f"how many {coin} are you inserting? : "))
        money += inserted * coins[coin]
    print(f"you are inserting {round(money, 2)} to the machine")
    return money


# TODO: 6 Check for a successful transaction
# a. See if the user has inserted enough money.
# b. If they have not inserted enough money refund the money.
# c. If the user has inserted enough money
#       - add that money as a resource. #
# d. If the user inserted too much money make change for the user.
# e. Change should be rounded to 2 decimal places.
def complete_transaction(cost, paid):
    """Checks to see if enough money is inserted to the machine. Will return a Boolean value. means there is enough
    money inserted. False means there is not enough money inserted. Will also calculate and return change the
    user is owed. """
    if paid > cost:
        # deposit money, make change.
        resources["money"] += cost
        print(f"refunding you {round(paid - cost, 2)}")
        return True
    elif paid == cost:
        # deposit money
        resources["money"] += cost
        return True
    else:
        # refund money
        print(f"refunding you {round(paid, 2)}, not enough inserted.")
        return False


# TODO: 7 Make the coffee
# a. Deduct the resources needed to make the coffee so the report will update next time it is run.
# b. Once all resources have been deducted tell the user "Here is your {drink}. Enjoy!" where {drink} is the
#    drink they chose.
def make_coffee(ingredients):
    """removes ingredients from resources (the available resources) and 'makes' the coffee. """
    
    for item in ingredients:
        resources[item] -= ingredients[item]
    return True


# TODO: 8 refill inventory
# extra feature to refill to original values for extra testing, or to refill contents as if it had been restocked.
def refill():
    """Test feature to refill the resources to full without restarting the program."""
    global resources
    money = resources["money"]
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": money,
    }


coffee_machine()
