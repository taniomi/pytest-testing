import pytest
import source.shapes as shapes


class TestRectangle:
    def test_area(self, rectangle):
        assert rectangle.area() == 200

    def test_perimeter(self, rectangle):
        assert rectangle.perimeter() == 60

    def test_not_equal(self, rectangle, weird_rectangle):
        assert rectangle != weird_rectangle
