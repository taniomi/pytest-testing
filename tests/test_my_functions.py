import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_add_strings():
    result = my_functions.add("Hello", " World")
    assert result == "Hello World"

def test_add_strings_fail():
    result = my_functions.add("Hello", "World")
    assert result == "Hello World"

def test_divide():
    result = my_functions.divide(1, 4)
    assert result == 0.25

def test_divide_by_zero():
    # We expect a ValueError to be raised
    # If a ValueError is raised, the test will pass
    # If the raised error is not a ValueError, the test will fail
    with pytest.raises(ValueError):
        my_functions.divide(1, 0)

def test_divide_by_zero_fail():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)
