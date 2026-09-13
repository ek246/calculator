
import pytest

from app.operations import addition, subtraction, multiplication, division
def test_addition():
    assert addition(2, 3) == 5
def test_subtraction(): 
    assert subtraction(5, 3) == 2
def test_multiplication():
    assert multiplication(2, 3) == 6
def test_addition_with_negative_numbers():
    assert addition(-2, -3) == -5
def test_subtraction_with_negative_numbers():
    assert subtraction(-5, -3) == -2
def test_multiplication_with_negative_numbers():
    assert multiplication(-2, -3) == 6
def test_division():
    assert division(6, 3) == 2
def test_division_with_negative_numbers():
    assert division(-6, -3) == 2
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(6, 0)  