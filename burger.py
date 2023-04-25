class Burger:
    base_price:float = 120
    base_ingredients:list[str] =["buns", "patty", "lettuce"]
    options :list[str]= ['cheese','luttice','Bacon']

    def __init__(self,name: str, size: str, price: float):
        self.name= name
        self.size = size
        self.price = price
    
    def get_ingredients(self):
        return self.base_ingredients
        
    @classmethod
    def veg_burger(cls):
        abj= cls.base_ingredients.append("onion")
        return abj

    def add_Bacon(self):
        self.base_price = self.base_price + 20
        self.base_ingredients.append("Bacon")

    def add_cheese(self):
        self.base_price = self.base_price + 10
        self.base_ingredients.append("Cheese")
        

    def add_lettuce(self):
        self.base_price = self.base_price + 30
        self.base_ingredients.append("lettuce") 
        

    @staticmethod
    def is_delicious():
        return  "base_ingredients"

  
    
# burger=Burger('hh','xl','100')
# burger.get_ingredients()                                                                    
# burger.veg_burger()
# burger.add_Bacon()
# burger.add_cheese()
# burger.add_luttice()
# burger.is_delicious(base_ingredients="")


    
