import random

import math

QUARTERS = 0.25
PENNIES = 0.01
DIMES = 0.10
NICKELS = 0.05

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


# TODO: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer

# TODO: Turn off the Coffee Machine by entering “ off ” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens


# TODO: Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# TODO: Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

def prepare_drink(choice):
    if choice == 'espresso':
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["milk"] -= MENU["espresso"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif choice == 'cappuccino':
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    elif choice == 'latte':
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]








def get_cost(choice):
    if choice == 'espresso':
        return MENU['espresso']['cost']
    elif choice == 'latte':
        return MENU["latte"]['cost']
    elif choice == 'cappuccino':
        return MENU['cappuccino']['cost']
    else:
        return 0


def return_change(money,choice):
        return f'{money - get_cost(choice):.2f}'


def calculate_money(quarters,pennies,nickels,dimes):
    return (quarters * QUARTERS) + ( pennies * PENNIES) + (nickels * NICKELS) + (dimes * DIMES)


def check_resources(choice):
    if choice == 'espresso':
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, there isn't enough water")
            return 0
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, there isn't enough coffee")
            return 0

    elif choice == 'cappuccino':
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry, there isn't enough water")
            return 0
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry, there isn't enough milk")
            return 0
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry, there isn't enough coffee")
            return 0

    elif choice == 'latte':
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry, there isn't enough water")
            return 0
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry, there isn't enough milk")
            return 0
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry, there isn't enough coffee")
            return 0






checker = True

while checker:

    user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if user_choice == 'off':
        checker = False
        print(resources)
        continue

    elif user_choice == 'report':
        print(f"The remaining resources are:\n"
              f"Water: {resources['water']}\n"
              f"Milk: {resources['milk']}\n"
              f"Coffee: {resources['coffee']}\n"
              f"Money: {resources['money']}\n")
        continue

    if check_resources(user_choice) == 0:
        continue

    print(f"Insert your coins.")

    quarters_inserted = int(input("How many quarters?: "))
    nickels_inserted = int(input("How many nickels?: "))
    dimes_inserted = int(input("How many dimes ?: "))
    pennies_inserted = int(input("How many pennies?: "))

    money = calculate_money(quarters_inserted,pennies_inserted,nickels_inserted,dimes_inserted)
    if money < get_cost(user_choice):
        print("Sorry not enough money, your order has been refunded.")

    elif money >= get_cost(user_choice):
        print(f"Here is your {user_choice} ☕️. Enjoy !")
        print(f"Here is your change ${return_change(money,user_choice)}")
        resources["money"] += get_cost(user_choice)
        prepare_drink(user_choice)





