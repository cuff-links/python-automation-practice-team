import pytest
from src.arithmetic.arithmetic import *

@pytest.mark.parametrize('a,b,expected', [
    (1, 8, 9),
    (3,17,20),
    (15, 22, 37), 
    (99, 1, 100),
    (-5, 6, 1),
    (-5, -5, -10)
])
def test_add(a,b,expected):
    assert addition(a, b) == expected
    
@pytest.mark.parametrize('a,b,expected', [
    (17, 8, 9),
    (37,17,20),
    (59, 22, 37), 
    (101, 1, 100),
    (-5, -5, 0),
    (3, -7, 10)
])
def test_subtraction(a, b, expected):
    assert subtraction(a, b) == expected