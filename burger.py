class Burger:
    base_price: float = 150
    base_ingredients: dict[str,int] = {'buns': 100, "patty": 50}
    options: dict[str, int] = {'cheese': 40, 'lettuce': 50, 'tomatoes': 55, 'pickles':45 }
    option2: dict[str, int] = {'chicken': 40, 'buff': 60, 'mutton': 90}

   
   
    def __init__(self):
        self.total_price: int = self.base_price




    def base_cost(self):
        print( f"your intial price is {self.base_ingredients['buns'] + self.base_ingredients['patty']}")
        self.total_price: int = self.base_ingredients['buns'] + self.base_ingredients['patty']
    

    def choose(self):
        choice: str = input("Do you want veg burger or non veg burger :  ")

        if choice == "veg":
            self.veg()

        elif choice == "nonveg":
            self.nonveg()
        
        else:
            print(f" Your normal price is {self.base_price}")


    def veg(self):
        print("Menu")
        for key,value in self.options.items():
            print(key ,":", value)
        x: str = input("What you want to add:  ")
        self.base_ingredients[x]=self.options[x]
        self.total_price: int = self.total_price + self.options[x]
        #print(self.total_price)
        result: str = input("Do you want to add more (y or n):  ")
        if result == "y":
             self.veg()
        elif result == "n":
            print(f"Your total price is {self.total_price}")
            
            print("," .join(self.base_ingredients.keys()))
        
    def nonveg(self):
        print("Menu")
        for key,value in self.option2.items():
            print(key ,":", value)
        x: str = input("What you want to add:  ")
        self.total_price: int = self.total_price + self.option2[x]
        self.base_ingredients[x]= self.option2[x]
        result: str = input("Do you want to add more (y or n):  ")
        if result == "y":
             self.nonveg()
        elif result == "n":
            print(f"Your total price is {self.total_price}")
            print("," .join(self.base_ingredients.keys()))








    





