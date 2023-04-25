from main2 import Burger


class Test:
        
    def test_select_options(self):
        bur = Burger()
        bur.select_options('veg')
        assert bur.ingredients == ['buns','veg_patty', 'lettuce', 'tomato', 'onion', 'cheese', 'mayonnaise', 'ketchup','buns']


    def test_show_extra_ingredients(self):
        bur1=Burger()
        bur1.show_extra_ingredients()
        assert bur1.EXTRA_INGREDIENTS == ['pickles', 'jalapenos', 'bacon', 'avocado','lettuce', 'tomato', 'onion', 'cheese', 'mayonnaise', 'ketchup']


    def test_add_extra_ingredients(self):
        bur2=Burger()
        bur2.add_extra_ingredient(1)
        assert bur2.ingredients == ['buns','pickles']

    def test_add_extra_ingredients_jalalpenos_pickles(self):
        bur2=Burger()
        bur2.add_extra_ingredient(2)
        bur2.add_extra_ingredient(7)
        assert bur2.ingredients == ['buns','jalapenos','onion']
    
    def test_select_extra_ingredients_test_price_increase(self):
        bur4= Burger()
        bur4.show_extra_ingredients()
        assert bur4.BASE_PRICE== bur4.price

    def test_select_extra_ingredients(self):
        bur3 = Burger()
        bur3.select_extra_ingredients()
        assert bur3.ingredients == ['buns', 'buns']

