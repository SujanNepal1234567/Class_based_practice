import pytest
from burger import Burger

def test_burger():
    burger = Burger("hh", "xl", 100)
    
    assert burger.get_ingredients() == ["buns", "patty", "lettuce"]

    veg_burger = Burger("hh", "xl", 100)
    assert veg_burger.get_ingredients() == ["buns", "patty", "lettuce"]
    

    burger.add_Bacon()
    assert burger.get_ingredients() == ["buns", "patty", "lettuce", "Bacon"]
    assert burger.base_price == 140

    burger.add_cheese()
    assert burger.get_ingredients() == ["buns", "patty", "lettuce", "Bacon", "Cheese"]
    assert burger.base_price == 150

    burger.add_lettuce()
    assert burger.get_ingredients() == ["buns", "patty", "lettuce", "Bacon", "Cheese", "lettuce"]
    assert burger.base_price == 180

    
    assert burger.is_delicious() == "base_ingredients"



