from decoretor_Burger import Burger
def test_burger():
    chicken=Burger()
    assert chicken._count_burger == 1
    assert chicken.total_patties == 3
    assert chicken.get_burger_number() == 1

def test_price(): 
    veg=Burger()
    assert veg._count_burger == 2
    assert veg.total_patties == 3
    veg.add_Cheese()
    assert veg.base_price == 210

def test_add_Bacon():
    bug=Burger()
    bug.add_Bacon()
    assert bug.base_price == 200
    assert bug.base_ingredient == ["Bun","Onions","Tomato Sauce","Patties","Bacon","Bun"]
    assert bug.count_ingredient == 6

def test_add_Cheese():
    burg=Burger()
    burg.add_Cheese()
    assert burg.base_price == 210
    assert burg.base_ingredient == ["Bun","Onions","Tomato Sauce","Patties","Cheese","Bun"]
    assert burg.count_ingredient == 6

def test_add_new_patty():
    bug2=Burger()
    bug2.add_new_patty()
    assert bug2.base_price == 180
    assert bug2.base_ingredient ==["Bun","Onions","Tomato Sauce","Patties","New Patty","Bun"]
    assert bug2.count_ingredient == 6

def test_mayo_sauce():
    bug3=Burger()
    bug3.add_mayo_sauce()
    assert bug3.base_price == 200 
    assert bug3.base_ingredient ==["Bun","Onions","Tomato Sauce","Patties","Mayo Sauce","Bun"]
    assert bug3.count_ingredient == 6

def test_find_name_of_restaurant(capsys):
    Burger.find_name_of_restaurant()
    captured = capsys.readouterr()
    assert captured.out == "The name of the restaurant is: Hello restaurant\n"

def test_get_burger_number():
    burger1 = Burger()
    burger2 = Burger()
    burger3 = Burger()
    assert Burger.get_burger_number() == 9

def test_multiple_price(): 
    specialburger=Burger()
    specialburger.add_Bacon()
    specialburger.add_Cheese()
    specialburger.add_mayo_sauce()
    specialburger.add_Cheese()
    assert specialburger.base_price == 370
    assert Burger.get_burger_number() == 10

    
