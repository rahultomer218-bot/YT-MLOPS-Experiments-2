import pytest
def square(x):
    return x * x

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0   

def cube(x):
    return x * x * x    

def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27
    assert cube(0) == 0 

def fifth_power(x):
    return x * x * x * x * x    
def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(3) == 243
    assert fifth_power(0) == 0  
def invalid_input(x):
    if x < 0:
        raise ValueError("Negative numbers are not allowed")
    return x
def test_invalid_input():
    with pytest.raises(ValueError):
        invalid_input(-1)   
    assert invalid_input(0) == 0
    assert invalid_input(5) == 5    
    