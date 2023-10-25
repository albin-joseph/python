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

profit = 0.0

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
    if(cost_for_drink > accepted_amount):
        return False
    else:
        balance = accepted_amount - cost_for_drink
        global profit 
        profit += cost_for_drink
        if(balance > 0):
            print(f"You have balance ${round(balance,2)}")
        return True
    

def make_drink(drink_name):
    ingradients = menu[drink_name]['ingredients']
    for key in ingradients:
        resources[key] -= ingradients[key]
    print(f"Please enjoy {drink_name}")
    

def run_machine():
    is_on = True
    while(is_on):
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if(choice == 'espresso' or choice == 'latte' or choice == 'cappuccino'):
            if(is_suffient_resources(choice)):
                accepted_amount = accept_money()
                if(is_amount_sufficient_for(choice, accepted_amount)):
                    make_drink(choice)
                else:
                    print('Amount is not sufficient.')
            else:
                print('Sorry, resources not available.')
        elif(choice == 'report'):
            print_report()
        elif(choice == 'off'):
            is_on = False
        else:
            print('Not a valid input')
        
run_machine()