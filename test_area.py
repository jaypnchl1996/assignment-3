import pytest  
from area import calculate_area_square  
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])

def test_calculate_area_square_positive():
    # Test for positive integer input
    assert calculate_area_square(9) == 81

def test_calculate_area_square_positive():
    # Test for positive integer input
    assert calculate_area_square(99) == 9801

  
