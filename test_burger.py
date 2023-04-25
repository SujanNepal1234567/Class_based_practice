from burger import Burger

def test_initial_burger_cost():

        burger1 = Burger()
        assert burger1.base_price == 150

def test_burger_ingredients():
        burger1= Burger()
        burger1.veg()
        assert burger1.total_price >= 150

def check_all_nonveg_ingredients():
        burger1 = Burger
        




