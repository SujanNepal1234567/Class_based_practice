# A burger class

class Burger:
    """
    A class to represent a burger.
    
    Atrributes:
        __base_price (float): The base price of the burger.
        __base_ingredients (list): List of base ingredients.
        burger_menu (dict): Menu of available burger types.
        
    Methods:
        show_menu: Display the available burger types along with it's ingredients.
        place_order: Place order for the burger available in menu.
        make_burger: Make burger and display the price.
    """
    
    # Class Variables (fields)
    # "__fieldname" represents private fields
    burger_menu: dict[str, list[str]] = {
        "Cheese Burger": ["Beef patty", "Cheese", "Ketchup", "Mustard"],
        "Veggie Burger": ["Veggie patty", "Onion", "Mayonnaise"],
        "Chicken Burger": ["Chicken patty", "Mayonnaise", "Pickles"],
        "Fish Burger": ["Fish patty", "Tartar sauce", "Pickles"]
    }
    
    __base_ingredients: list[str] = ["Bun", "Tomato", "Lettuce", ]  # Private class method
    
    # Constructor
    def __init__(self) -> None:
        """
        Initializes a new instance of the Burger class.
        """
        self.base_price: float = 5  # Instance variable
    
    # Class method to print burger menu
    @classmethod
    def show_menu(cls) -> None:
        """
        Prints the menu of available burgers and their ingredients.
        
        This is a class method.
        
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
    
    # Instance method to place order
    def place_order(self, burger_type: str) -> None:
        """
        Places an order for a burger and calculates the price and ingredients of the burger.
        
        Args:
            self: The object pointer.
            burger_type (str): Type of burger that is to be ordered

        Returns:
            None.
            
         Raises:
            ValueError: If the burger_type is not available in the burger menu.
        """
        if burger_type not in Burger.burger_menu:
            raise ValueError(f"{burger_type} is not available in the burger menu.")
        
        self.burger_type = burger_type
        self.ingredients = list(set(self.__base_ingredients + self.burger_menu[burger_type]))
        self.price = self.base_price + 5
        print(f"\nYou have ordered a {self.burger_type} for {self.price} dollars.")
    
    # Instance method to make burger
    def make_burger(self) -> None:
        """
        Makes a burger and prints a message indicating that the burger is ready.
        
        Args:
            self: The object pointer.

        Returns:
            None.
            
        Raises:
            None.
        """
        print(f"\nMaking your {self.burger_type} burger with ingredients => {', '.join(self.ingredients)}.")
        print("\nDone! Enjoy your burger!\n")
        
    # Static method to give feedback
    @staticmethod
    def submit_feedback() -> None:
        """
        A static method to submit feedback.

        Args:
            None.

        Returns:
            None.
        
        Raises:
            None.
        """
        feedback_prompt = input("How was your burger? \n=> ")
        print("\nFeedback Submitted. Thank you!!!") 