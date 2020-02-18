"""
Unit tests for the calculator library
"""
import calculator


class TestCalculator:

    def test_addition(self):
        assert calculator.add(2, 3) == 5

    def test_subtraction(self):
        assert calculator.subtract(7, 4) == 3
