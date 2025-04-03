import pytest
import source.shapes as shapes


"""
The conftest.py file is used to share fixtures across multiple files.

Fixtures defined here are available to all test files.
"""

@pytest.fixture
def rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5, 6)