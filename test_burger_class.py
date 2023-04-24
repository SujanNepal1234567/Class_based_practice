from burger import Burger
import pytest

def test_place_order():
    burger = Burger()
    burger.place_order("Cheese Burger")
    assert burger.burger_type == "Cheese Burger"
    assert set(burger.ingredients) == set(['Lettuce', 'Mustard', 'Tomato', 'Ketchup', 'Beef patty', 'Cheese', 'Bun'])
    assert burger.price == 10
    
def test_place_order_with_invalid_burger_type():
    burger = Burger()
    with pytest.raises(ValueError, match="Invalid Burger is not available in the burger menu."):
        burger.place_order("Invalid Burger")
        
# def test_submit_feedback(capsys, monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: "Delicious")
#     Burger.submit_feedback()
#     captured = capsys.readouterr()
#     assert captured.out == "\nFeedback Submitted. Thank you!!!\n"