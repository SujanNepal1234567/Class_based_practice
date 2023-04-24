# library imports
from os import system
from burger import Burger

def program():
    # clears terminal before printing output
    system("clear")
    
    # class method to print the available menu
    Burger.show_menu()
    
    # instantiating Burger class
    burger = Burger()

    # takes prompt from user to place order
    order_prompt = input("\nEnter your order: ").title()
    
    # instance method to place order available in the menu
    burger.place_order(order_prompt)

    # instance method to make burger for the order placed
    burger.make_burger()
    
    # static method to take feedback from the customer
    Burger.submit_feedback()
    
    # print(Burger.burger_menu)    
    
if __name__ == "__main__":
    program()
