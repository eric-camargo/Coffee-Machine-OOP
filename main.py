from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

available_options = my_menu.get_items()
on = True

while on:
    choice = input(f"What would you like? ({available_options}): ").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        selection = my_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(selection):
            if my_money_machine.make_payment(selection.cost):
                my_coffee_maker.make_coffee(selection)
