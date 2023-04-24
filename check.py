from burger import Burger

# print(Burger.__base_ingredients) # private class variable not accessed

print(Burger.burger_menu) # class variable accessed

# Burger.place_order("Fish Burger") # instance variable not accessed

# Burger.make_burger() # instance variable not accessed 

Burger.show_menu() # class method accessed

# instance variable "base_price" set to 5 
burger = Burger()

print(burger.base_price) # instance variable accessed

print(burger.burger_menu) # class variable accessed by instance

burger.place_order("Fish Burger") # instance method with argument accessed

burger.make_burger() # instance method without argument accessed



