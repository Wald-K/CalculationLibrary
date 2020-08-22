"""
Unit tests for the calculator library
"""
import calculator


class TestCalculator:

    def test_addition(self):
        assert calculator.add(2, 3) == 5

    def test_subtraction(self):
        assert calculator.subtract(7, 4) == 3

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_power(self):
        assert 1000 == calculator.power(10, 3)
