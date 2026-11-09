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
#Get input from user on what drink they want
#Calculate the amount of resources left
#Calculate the coin
def coin_calculation(quarters,dimes,nickles,pennies,user_choice):
    total_coin = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    print(total_coin)

    if total_coin < MENU[user_choice]["cost"]:
        return f"Sorry, you don't have enough money to buy {user_choice}"
    elif total_coin > MENU[user_choice]["cost"]:
        balance = total_coin - MENU[user_choice]["cost"]
        return f"Here is the change ${balance}\nHere is your {user_choice},Enjoy!"
    else:
        return f"HERE IS YOUR {user_choice},ENJOY!"
def coffee_in(user_choice):
    global resources
    drink_ingredients = MENU[user_choice]["ingredients"]
    # Safely replaces values in the resource dictionary for only the ingredients needed
    for ingredient, amount in drink_ingredients.items():
        resources[ingredient] -= amount
    return resources
def is_ingredient_suff(user_choice):
    global resources  # Forces Python to check the accurate global resource dict
    drink_ingredients = MENU[user_choice]["ingredients"]
    for item, amount_needed in drink_ingredients.items():
        if resources[item] < amount_needed:
            print(f"Sorry, there is not enough {item}!")
            return False
    return True





coffee_machine=True

while coffee_machine is not False:
    choice = input("What would you like?(espresso/latte/cappuccino):").lower()

    if choice=="report":
        for key, value in resources.items():
            print(f"{key} -> {value}")
    elif choice=="off":
        coffee_machine=False
    elif choice=="espresso" or choice=="latte" or choice=="cappuccino":
        if is_ingredient_suff(choice):
            print("Please insert coins.")
            coin_quart=float(input("How many quarts?:"))
            coin_dimes=float(input("How many dimes?:"))
            coin_nickles=float(input("How many nickles?:"))
            coin_pennies=float(input("How many pennies?:"))



            result=coin_calculation(coin_quart,coin_dimes,coin_nickles,coin_pennies,choice)
            print(result)

            if "Sorry" not in result:
                coffee_in(choice)
    else:
        print("Invalid entry. Please choose espresso, latte, or cappuccino.")