"""
Unit tests for the calculator library
"""

import calaculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calaculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calaculator.subtract(4, 2)