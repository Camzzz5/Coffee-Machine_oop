from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
me =  Menu()
a=True
while a:    
    options = me.get_items()
    order_name = input(f"What would you like? {options}")
    if order_name == "off":
        a=False
    elif order_name == "report":
        #Print all the resources from  the machine to the screen
        print("Printing report of ingredients and money")
        coffeemaker.report()
        moneymachine.report() 
    elif order_name in options:     
        status = coffeemaker.is_resource_sufficient(me.find_drink(order_name))
        if status == False:
            break
        moneymachine.make_payment(me.find_drink(order_name).cost)
        coffeemaker.make_coffee(me.find_drink(order_name))
    else:
        print("Enter a valid name")