# decoretor_Burger.py
# import sys
# from pydantic import Field, BaseModel


# class Patty:
#     def ___init__(self, type_, price):
#         self.type_ = type_
#         self.price = price

# class AbstractBurger:
#     def add_patty(self, patty: Patty):


class Burger():
    """
    A class representing a burger with basic ingredients.
    """
    _count_burger : int = 0
    total_patties = 3 

    def __init__(self) -> None:
        """
        Initialize a new burger instance with a base price, count of ingredients,
        and a list of base ingredients. Increment the class count of burgers by 1.
        """
        self.base_price : int = 150
        self.count_ingredient: int = 5
        self.base_ingredient : list[str] = ["Bun","Onions","Tomato Sauce","Patties","Bun"]
        Burger._count_burger += 1

    @classmethod
    def get_burger_number(cls) -> int:
        """
        A class method that prints the current count of burger instances.
        """
        # print(cls._count_burger)
        return cls._count_burger

    def add_Bacon(self):
        """
        A method that adds bacon to the burger, increases the base price, and 
        increments the count of ingredients.
        """
        self.base_price = self.base_price + 50
        print(f"this is of bacon{self.base_price}")
        self.base_ingredient.insert(-1,"Bacon")
        self.count_ingredient += 1
    
    def add_Cheese(self):
        """
        A method that adds cheese to the burger, increases the base price, and 
        increments the count of ingredients.
        """
        self.base_price = self.base_price + 60
        self.base_ingredient.insert(-1,"Cheese")
        self.count_ingredient += 1

    def add_new_patty(self):
        """
        A method that adds a new patty to the burger, increases the base price, and 
        increments the count of ingredients.
        """
        self.base_price = self.base_price + 30
        self.base_ingredient.insert(-1,"New Patty")
        self.count_ingredient += 1

    def add_mayo_sauce(self):
        """
        A method that adds mayo sauce to the burger, increases the base price, and 
        increments the count of ingredients.
        """
        self.base_price = self.base_price + 50
        self.base_ingredient.insert(-1,"Mayo Sauce")
        self.count_ingredient += 1

    def return_burger(self):
        """
        A method that prints information about the burger instance, including its price,
        ingredients, the number of ingredients, and the number of burger instances created.
        """
        print(f"The Burger is priced at $ {self.base_price}")
        print(f"The Burger is as {self.base_ingredient}")
        print(f"This is the {Burger._count_burger} of the day")
        print(f"This has {self.count_ingredient} number of ingredients")
    
    @staticmethod
    def find_name_of_restaurant():
        """
        A static method that prints the name of the restaurant.
        """
        print("The name of the restaurant is: Hello restaurant")

if __name__ == '__main__':
    # Example usage
    chicken=Burger()
    # chicken.add_Bacon()
    chicken.add_Bacon()
    chicken.add_Cheese()
    chicken.return_burger()
    # chicken2=Burger()
    # chicken2.add_Bacon()
    # chicken2.add_Cheese()
    # # print(Burger.count_burger)
    # Burger.get_burger_number()
    # Burger.find_name_of_restaurant()
    # chicken2234324=Burger()
    # chicken2234=Burger()
    # chicken23=Burger()
    # chicken223=Burger()
    # chicken23=Burger()
    # Burger.get_burger_number()
    print(chicken.base_ingredient)


        # if self.base_price < 100: 
        #     raise ValueError("Value is less than 100")
        # else:
        #     return



    # base_ingredient : list[str] = ["Bun","Onions","Tomato Sauce","Patties","Bun"]
    # extra_ingredient : list[str] = ["Cheese","Bacon","Mayo Sauce","New Patty"]

    # def __new__(cls,price) -> None:
    #     if price < cls.base_price:
    #         raise ValueError("Value is less than 100")
    #     else: 
    #         return super().__new__(cls)
    
    # def __new__(cls) -> Self:
    #     return super().__new__()
    
    
    # @property 
    # def add_patties(self) :
    #     print(self.total_patties)
    
    # @add_patties.setter
    # def add_patties(self,number:int) :
    #     self.total_patties += number 