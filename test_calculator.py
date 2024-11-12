"""
Unit tests for the calculator library
"""

import calaculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calaculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calaculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calaculator.multiply(10, 10)


# Ensure the file ends with a newline
