import pytest
from square_area import calculate_square_area

def test_calculate_square_area():
    # Existing unit test
    assert calculate_square_area(5) == 25

    # New unit test
    # Use the last two digits of your student ID as the expected output
    # For demonstration, let's assume the last two digits are 42
    assert calculate_square_area(6) == 36  # Modify input to make the test fail
