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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

loop = False
revenue = 0.0


# TODO: 2. Check resources sufficient?:
def check_resources(user_input):
    for items in user_input:
        if resources[items] < user_input[items]:
            print("Sorry There is not enough water")
            return 0
    return 1

def coins_calculation(cost, requirements):
    global revenue, resources
    quarters = float(input("How many quarters do you have?")) * 0.25
    dimes = float(input("How many dimes do you have?")) * 0.10
    nickels = float(input("How many dimes do you have?")) * 0.05
    pennies = float(input("How many pennies do you have?")) * 0.01

    if cost <= (quarters + dimes + nickels + pennies):

        revenue += float(cost)

        for items in requirements:
            resources[items] -= requirements[items]

            if resources[items] < 0:
                resources[items] += requirements[items]
                print(f"Sorry {items} is out ")

        return 0

    elif cost > (quarters + dimes + nickels + pennies):

        print("You don't have money enough ")
        print("coins are refunded")

        return True


# TODO: 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):

while not loop:

    user_input = input(" What would you like? (espresso/latte/cappuccino):")
    check_1 = 0

    if user_input.lower() == "off":

        loop = True

    elif user_input.lower() == "report":

        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${revenue}")

    elif user_input.lower() == 'espresso' or user_input.lower() == 'latte' or user_input.lower() == 'cappuccino':
        check_1 = check_resources(MENU[user_input]['ingredients'])
    if check_1 == 1:
        loop = coins_calculation(MENU[user_input]['cost'],MENU[user_input]['ingredients'])