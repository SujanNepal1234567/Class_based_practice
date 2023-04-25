class Burger:
    BASE_PRICE: float = 5.0
    BASE_INGREDIENTS: list[str] = ['buns']
    OPTIONS: dict[str, list[str]] = {
        'veg': ['veg_patty', 'lettuce', 'tomato', 'onion', 'cheese', 'mayonnaise', 'ketchup'],
        'chicken': ['chicken_patty', 'lettuce', 'tomato', 'onion', 'cheese', 'mayonnaise', 'ketchup'],
        'beef': ['beef_patty', 'lettuce', 'tomato', 'onion', 'cheese', 'mayonnaise', 'ketchup']
    }
    EXTRA_INGREDIENTS: list[str] = ['pickles', 'jalapenos', 'bacon', 'avocado','lettuce', 'tomato', 'onion', 'cheese', 'mayonnaise', 'ketchup']

    def __init__(self):
        self.price = self.BASE_PRICE
        self.ingredients = self.BASE_INGREDIENTS.copy()

    def select_options(self, option: str):
        if option not in self.OPTIONS:
            print(f"Invalid option. Available options are: {', '.join(self.OPTIONS)}")
            return
        self.ingredients += self.OPTIONS[option]
        self.select_extra_ingredients()

    def select_extra_ingredients(self):
        while True:
            ans = input("Do you want to add any extra ingredient (y/n)? ").lower()
            if ans == 'y':
                self.show_extra_ingredients()
                ingredient = input(f"Enter the number of the ingredient you want to add (0 to cancel): ")
                if not ingredient.isdigit() or int(ingredient) not in range(len(self.EXTRA_INGREDIENTS)+1):
                    print(f"Invalid input. Please enter a number between 0 and {len(self.EXTRA_INGREDIENTS)}.")
                    continue
                elif int(ingredient) == 0:
                    break
                else:
                    self.add_extra_ingredient(int(ingredient))
            elif ans == 'n':
                self.ingredients.append("buns")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        print(f"Ingredients selected: {', '.join(self.ingredients)}")
        print(f"Total price: {self.price}")

    def show_extra_ingredients(self):
        print("Available extra ingredients:")
        for i, ingredient in enumerate(self.EXTRA_INGREDIENTS, start=1):
            print(f"{i}. {ingredient}")

    def add_extra_ingredient(self, ingredient_num):
        ingredient = self.EXTRA_INGREDIENTS[ingredient_num - 1]
        self.ingredients.append(ingredient)
        self.price += 2.0 if ingredient in self.EXTRA_INGREDIENTS[:3] else 0.5

def main():
    bur = Burger()
    bur.select_options(input("Enter your option: "))

if __name__ == "__main__":
    main()

