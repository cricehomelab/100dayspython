from D16_menu import Menu, MenuItem
from D16_coffee_maker import CoffeeMaker
from D16_money_machine import MoneyMachine

brewer = CoffeeMaker()
options = Menu()
coin_box = MoneyMachine()

LIST_OF_DRINKS = ['latte', 'espresso', 'cappuccino']

running = True
while running:
    get_input = input(f"What would you like to drink {options.get_items()}? ").lower()
    # stops the loop
    if get_input == "off":
        running = False
    # prints a report
    elif get_input == "report":
        print(brewer.report())
    else:
        if get_input in LIST_OF_DRINKS:
            # available will be equal to True or False
            available = brewer.is_resource_sufficient(options.find_drink(get_input))
            #print(f"Will be 'True' if available {available}")
            # if the item is available take payment and make coffee
            if available:
                drink = vars(options.find_drink(get_input))
                #print(f'this {drink["cost"]} is made of {drink}')
                print(f"Your drink will cost {drink['cost']}.")
                # checks for money being inserted.
                if coin_box.make_payment(drink["cost"]):
                    #print(drink["ingredients"])
                    # wasn't sure why this didn't work at first turns out this has to be an attribute. It can't just be the
                    # same data outside an attribute.
                    #brewer.make_coffee(drink)
                    # this works for some reason
                    brewer.make_coffee(options.find_drink(get_input))
        else:
            print("that is not a valid option.")













