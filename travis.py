import pytest

def func(x):
    return x+8
    
    
def test_method():
    assert func(1) == 9