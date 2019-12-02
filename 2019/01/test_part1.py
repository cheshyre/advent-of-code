"""Module to test given examples from part 1."""
import unittest

import fuel_calculator


class TestFuelCalculator(unittest.TestCase):
    """Class to test basic cases for fuel requirements."""

    def test_fuel_mass_12(self):
        """Check fuel(12) -> 2."""
        self.assertEqual(fuel_calculator.get_fuel_needed(12), 2)

    def test_fuel_mass_14(self):
        """Check fuel(14) -> 2."""
        self.assertEqual(fuel_calculator.get_fuel_needed(14), 2)

    def test_fuel_mass_1969(self):
        """Check fuel(1969) -> 654."""
        self.assertEqual(fuel_calculator.get_fuel_needed(1969), 654)

    def test_fuel_mass_100756(self):
        """Check fuel(100756) -> 33583."""
        self.assertEqual(fuel_calculator.get_fuel_needed(100756), 33583)
