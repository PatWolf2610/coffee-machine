import re
from unicodedata import name

from numpy import False_


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
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def payment_process(order_cost):
    print("Please insert coin!!")
    quarter  = int(input("How many quarters ?" )) # quater = 0.25$
    dimes = int(input("How many dimes ?")) # dimes  0.10
    nickles = int(input("How many nickles ?")) # nickles = 0.05
    pennies = int(input("How many pennies ?")) # pennies = 0.01
    total = quarter*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    if total < order_cost:
        print("Sorry, there is not enough money, money refund")
        return False
    else: 
        print("Transaction sucessful")
        print(f"Here is {total - order_cost} money in change")
        return True

def resource_trigger(order_ingredients,resource_left):
    for item in order_ingredients:
            resource_left[item] = resource_left[item] - order_ingredients[item]
    else:
        pass
    print(resource_left)
    return resource_left 

def money_trigger(order_cost,money):
    money = money + order_cost
    return money

def resource_produce(resource_left):
    water = int(input("How much water ?"))
    milk = int(input("How much milk?"))
    coffee = int(input("How much coffee?"))
    resource_add = {
        "water":water,
        "milk":milk,
        "coffee": coffee
    }
    for item in resource_left:
        resource_left[item] = resource_left[item] + resource_add[item]
    return resource_left
        




profit = 0
is_on = True
while is_on :
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
        print(f"Money : {profit}")
    elif choice == 'latte' or choice == 'espresso' or choice =="cappuccino" :
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            if payment_process(drink['cost']):
                resources = resource_trigger(drink["ingredients"],resources)
                profit = money_trigger(drink["cost"],profit)
                print(f"Here is your {choice}")
    elif choice == 'add':
        resources = resource_produce(resources)
    else:
        print("Invalid order")



            

        



