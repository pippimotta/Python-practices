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
    "coffee": 100
}

profit = 0
def coffee_check(coffee):
    coffee_kind_ingredients = MENU[coffee]['ingredients']
    for ingredient in coffee_kind_ingredients:
        if coffee_kind_ingredients[ingredient] > resources[ingredient]:
            print(f'Sorry,there is not enough {ingredient}')
            return False
        else:
            return True


def bill(coffee):
    global profit#活用global
    coffee_price = MENU[coffee]['cost']
    insert_coins = insert_coin()
    if insert_coins < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        return False

    else:
        profit += coffee_price
        if insert_coins > coffee_price:
            change = round(insert_coins - coffee_price, 2)
            print(f"Here is ${change} dollars in change.\nHere is your {coffee} ☕️.Enjoy! ")
            return True #活用返回值

def insert_coin():
    print('Please insert coins')
    quarters_number = int(input('how many quarters?:'))
    dimes_number = int(input('how many dimes?:'))
    nickles_number = int(input('how many nickles?:'))
    penny_number = int(input('how many pennies?:'))
    total = quarters_number * 0.25 + dimes_number * 0.1 + nickles_number * 0.05 + penny_number * 0.01
    return total


def coffee_machine():
    not_end = True
    while not_end:
        menu = input("What would like? (espresso/latte/cappuccino)\n(Enter 'report' to check the tank) : ")
        if menu == 'report':
            water = resources['water']
            milk = resources['milk']
            coffee = resources['coffee']
            print(f"Water: {water}ml\nMilk:{milk}ml\nCoffee:{coffee}g\nMoney:${profit}")
        else:
            if coffee_check(menu):
                if bill(menu):
                    for ingredient in MENU[menu]['ingredients']:
                        resources[ingredient] -= MENU[menu]['ingredients'][ingredient]
        if menu == 'end':
            not_end = False


coffee_machine()

