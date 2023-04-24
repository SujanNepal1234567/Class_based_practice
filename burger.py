# A burger class

class Burger:
    """
    A class to represent a burger.
    
    Atrributes:
        base_price (float): The base price of the burger.
        base_ingredients (list): List of base ingredients.
        burger_menu (dict): Menu of available burger types.
        
    Methods:
        show_menu: Display the available burger types along with it's ingredients.
        place_order: Place order for the burger available in menu.
        make_burger: Make burger and display the price.
    """
    
    # Class Variables (fields)
    base_price: float = 5
    base_ingredients: list[str] = ["Bun", "Tomato", "Lettuce", ]
    burger_menu: dict[str, list[str]] = {
        "Cheeseburger": ["Beef patty", "Cheese", "Ketchup", "Mustard"],
        "Veggie Burger": ["Veggie patty", "Onion", "Mayonnaise"],
        "Chicken Burger": ["Chicken patty", "Mayonnaise", "Pickles"],
        "Fish Burger": ["Fish patty", "Tartar sauce", "Pickles"]
    }
    
    # Constructor
    def __init__(self):
        """
        Initializes a new instance of the Burger class.
        """
        pass
    
    # Static method to print burger menu
    @staticmethod
    def show_menu():
        """
        Prints the menu of available burgers and their ingredients.
        
        Args:
            None.

        Returns:
            None.
            
        Raises:
            None.
        """
        print("Burger Menu:")
        for burger_type, ingredients in Burger.burger_menu.items():
            print(f"{burger_type}: {', '.join(ingredients)}")
    
    # Method to place order
    def place_order(self, burger_type: str):
        """
        Places an order for a burger and calculates the price and ingredients of the burger.
        
        Args:
            self: The object pointer.
            burger_type (str): Type of burger that is to be ordered

        Returns:
            None.
            
        Raises:
            None.
        """
        self.burger_type = burger_type
        self.ingredients = list(set(self.base_ingredients + self.burger_menu[burger_type]))
        self.price = self.base_price + 5
        print(f"You have ordered a {self.burger_type} for {self.price} dollars.")
    
    # Method to make burger
    def make_burger(self):
        """
        Makes a burger and prints a message indicating that the burger is ready.
        
        Args:
            self: The object pointer.

        Returns:
            None.
            
        Raises:
            None.
        """
        print(f"Making your {self.burger_type} burger with ingredients => {', '.join(self.ingredients)}.")
        print("\nDone! Enjoy your burger!")
    
    