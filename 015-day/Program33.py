#It's a program challenge
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}
resources = {
    "water":100,
    "milk": 50,
    "coffee": 76
}

coins = {
    "quarters":{
        "value": 0.25
    },
    "dimes":{
        "value": 0.10
    },
    "nickles":{
        "value": 0.05
    },
    "pennies":{
        "value": 0.01
    }
}

profit = 0

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gm")
    print(f"Money: ${profit}")

def is_suffient_resources(drink_name):
    ingradients = menu[drink_name]['ingredients']
    for key in ingradients:
        if(resources[key] < ingradients[key]):
            return False
        else:
            continue
    return True

    
def accept_money():
    accepted_money = 0.0
    for key in coins:
        number_of_coins = input(f"How many number of {key} inserted: ")
        accepted_money += float(number_of_coins) * coins[key]['value']
    return accepted_money

def is_amount_sufficient_for(drink_name, accepted_amount):
    cost_for_drink = menu[drink_name]['cost']
    print(cost_for_drink)
    if(cost_for_drink > accepted_amount):
        return False
    else:
        return True
    

def make_drink():
    print('Enjoy the drink')


user_input = input("What would you like? (espresso/latte/cappuccino): ")
is_sufficient = is_suffient_resources(user_input)
if(user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino'):
    if(is_sufficient):
        print('Availa')
        accepted_amount = accept_money()
        print(f"accepted money: {accepted_amount}")
        is_sufficient_amount = is_amount_sufficient_for(user_input, accepted_amount)
        if(is_sufficient_amount):
            print('Amount enough')
            make_drink()
        else:
            print('Amount not enough refund')
    else:
        print('Sorry not avail')
elif(user_input == 'report'):
    print_report()
elif(user_input == 'Off'):
    exit
else:
    print('Not a valid input')